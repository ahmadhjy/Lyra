document.addEventListener("DOMContentLoaded", () => {
  initScrollReveal();

  const toggle = document.querySelector(".nav-toggle");
  const nav = document.querySelector(".site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      const open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  const chatFab = document.getElementById("chat-fab");
  const chatPanel = document.getElementById("chat-panel");
  const chatClose = document.getElementById("chat-panel-close");

  // Chat is disabled/hidden until the AI backend is integrated.
  if (!chatFab || !chatPanel || chatFab.hidden) return;

  const openChat = () => {
    chatPanel.hidden = false;
    chatPanel.setAttribute("aria-hidden", "false");
    chatPanel.classList.add("is-open");
    chatFab.setAttribute("aria-expanded", "true");
  };

  const closeChat = () => {
    chatPanel.classList.remove("is-open");
    chatPanel.setAttribute("aria-hidden", "true");
    chatFab.setAttribute("aria-expanded", "false");
    setTimeout(() => {
      if (!chatPanel.classList.contains("is-open")) {
        chatPanel.hidden = true;
      }
    }, 200);
  };

  chatFab.addEventListener("click", () => {
    if (chatPanel.classList.contains("is-open")) {
      closeChat();
    } else {
      openChat();
    }
  });

  if (chatClose) {
    chatClose.addEventListener("click", closeChat);
  }
});

function initScrollReveal() {
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    return;
  }

  const targets =
    ".section-header, .hero-copy, .hero-visual, .hero-stats, .hero-media-row, .card, " +
    ".approach-grid__left, .approach-grid__media, .cta-band-inner, .content-block, " +
    ".split > div, .page-hero__copy, .page-hero__media, .contact-grid > div, .panel, .steps";

  document.querySelectorAll("main section, main .page-hero").forEach((section) => {
    section.querySelectorAll(targets).forEach((el, index) => {
      el.classList.add("reveal");
      el.style.setProperty("--reveal-delay", `${Math.min(index * 80, 400)}ms`);
    });
  });

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -5% 0px" }
  );

  document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));
}
