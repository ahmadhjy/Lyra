# LYRA ↔ Matrix TRC — Referral Tracking Integration Guide

This guide explains how Matrix TRC reports course enrollments back to LYRA so both
sides have accurate referral records. It is a one-time setup on the Matrix TRC side.

---

## 1. How the referral flow works

1. A visitor browses the **AI Agora** page on `https://lyraaiqat.com/ai-agora/`.
2. When they click a course, LYRA records the click and redirects them to the course
   page on `matrixtrc.ai` with tracking parameters appended:

   ```
   https://www.matrixtrc.ai/course/<course-slug>?lyra_ref=<unique-id>&utm_source=lyraaiqat.com&utm_medium=referral&utm_campaign=ai-agora
   ```

   - `lyra_ref` is a unique UUID generated per click. This is the key value —
     it links a click on LYRA's site to an enrollment on yours.
3. If that visitor enrolls, Matrix TRC sends a webhook (below) to LYRA including the
   `lyra_ref` value. LYRA matches it to the original click and records the conversion.

## 2. What Matrix TRC needs to do

### Step A — Capture `lyra_ref` when the visitor lands

The `lyra_ref` query parameter must be stored when the visitor arrives, so it is
still available at enrollment time (visitors rarely enroll on the first page view).

Since your site runs on LearnWorlds, add this snippet in
**Site Builder → Settings → Custom Code (Head/Body)** so it runs on every page:

```html
<script>
(function () {
  var params = new URLSearchParams(window.location.search);
  var ref = params.get("lyra_ref");
  if (ref) {
    localStorage.setItem("lyra_ref", ref);
    document.cookie = "lyra_ref=" + ref + "; max-age=2592000; path=/"; // 30 days
  }
})();
</script>
```

Then attach the stored value to the user at signup — the simplest reliable option in
LearnWorlds is to write it into a **custom signup field** (hidden) or store it as a
**user tag** via your automation tool (Zapier / Make) when processing the signup event.

### Step B — Send the enrollment webhook to LYRA

When a user enrolls in (or purchases) a course, send an HTTP POST request:

- **URL:** `https://lyraaiqat.com/agora/webhook/enrollment/`
- **Method:** `POST`
- **Headers:**

  | Header | Value |
  |---|---|
  | `Content-Type` | `application/json` |
  | `X-Lyra-Webhook-Secret` | `VgBq1wJBu1mE3PBFdaDs6xfZzSdiv_9CJFCgvoZMBLE` |

- **JSON body:**

```json
{
  "lyra_ref": "the-uuid-captured-in-step-A",
  "course_slug": "designing-data",
  "event_type": "enrollment",
  "student_email": "optional@example.com",
  "enrolled_at": "2026-07-13T12:00:00Z"
}
```

Field notes:

| Field | Required | Description |
|---|---|---|
| `lyra_ref` | **Yes** | The UUID from the referral link. Without it the conversion cannot be matched. |
| `course_slug` | Recommended | The course slug as it appears in the URL, e.g. `data-management-and-sql`. |
| `event_type` | Optional | Defaults to `enrollment`. Use `purchase`, `free_signup`, etc. if you want to distinguish. |
| Anything else | Optional | The full payload is stored on LYRA's side, so extra fields are welcome. |

### Step C — Handle the response

| HTTP status | Meaning |
|---|---|
| `200` | Received and stored. Response body: `{"ok": true, "conversion_id": 123, "matched_click": true}` |
| `400` | Malformed JSON or missing `lyra_ref`. |
| `401` | Wrong or missing `X-Lyra-Webhook-Secret` header. |
| `503` | LYRA side not configured yet — contact LYRA. |

If you receive a non-200 response or a network error, please retry (e.g. up to 3
times with a delay). Duplicate sends are safe — LYRA stores each event.

## 3. Test the integration

You can verify connectivity any time with curl (no real enrollment needed):

```bash
curl -X POST https://lyraaiqat.com/agora/webhook/enrollment/ \
  -H "Content-Type: application/json" \
  -H "X-Lyra-Webhook-Secret: VgBq1wJBu1mE3PBFdaDs6xfZzSdiv_9CJFCgvoZMBLE" \
  -d '{"lyra_ref": "test-ping", "course_slug": "designing-data", "event_type": "test"}'
```

Expected response:

```json
{"ok": true, "conversion_id": 1, "matched_click": false}
```

(`matched_click` is `false` for a test ping because `test-ping` is not a real click ID.)

## 4. Implementation options within LearnWorlds

Pick whichever fits your setup:

1. **LearnWorlds native webhooks + Zapier/Make (easiest):** LearnWorlds can trigger
   on *"Enrolled in a course"* / *"Purchased a product"*. Route that trigger through
   Zapier or Make, look up the user's stored `lyra_ref` (custom field / tag), and send
   the POST request described in Step B.
2. **LearnWorlds API + your own script:** poll or receive enrollment events on your
   own backend and forward them to LYRA's endpoint.
3. **Custom checkout JS (least reliable, not recommended alone):** fire the webhook
   client-side on the thank-you page, reading `lyra_ref` from localStorage.

## 5. Security notes

- Keep the secret key private — it is the only authentication on this endpoint.
- Always send it in the `X-Lyra-Webhook-Secret` header, never in the URL.
- The endpoint only accepts `POST` over HTTPS.
- If the key is ever exposed, contact LYRA and we will rotate it.

## Contact

Technical contact: LYRA — info@lyraaiqat.com
