import uuid

from django.db import models


class AgoraReferralClick(models.Model):
    ref_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, db_index=True)
    course_slug = models.CharField(max_length=200)
    course_title = models.CharField(max_length=300)
    destination_url = models.URLField(max_length=500)
    clicked_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    session_key = models.CharField(max_length=64, blank=True)

    class Meta:
        ordering = ["-clicked_at"]
        verbose_name = "Agora referral click"
        verbose_name_plural = "Agora referral clicks"

    def __str__(self):
        return f"{self.course_slug} ({self.ref_id})"


class AgoraReferralConversion(models.Model):
    click = models.ForeignKey(
        AgoraReferralClick,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="conversions",
    )
    lyra_ref = models.CharField(max_length=64, db_index=True)
    course_slug = models.CharField(max_length=200, blank=True)
    event_type = models.CharField(max_length=50, default="enrollment")
    converted_at = models.DateTimeField(auto_now_add=True)
    payload = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ["-converted_at"]
        verbose_name = "Agora referral conversion"
        verbose_name_plural = "Agora referral conversions"

    def __str__(self):
        return f"{self.event_type} — {self.lyra_ref}"
