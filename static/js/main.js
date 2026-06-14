document.addEventListener("DOMContentLoaded", () => {
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

  if (!chatFab || !chatPanel) return;

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
