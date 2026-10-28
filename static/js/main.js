(function () {
  "use strict";

  // Mobile navigation
  const toggle = document.querySelector(".nav-toggle");
  const nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      const open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open);
      toggle.innerHTML = open ? '<i class="fa-solid fa-xmark"></i>' : '<i class="fa-solid fa-bars"></i>';
    });
  }

  // Toast notifications
  const toastWrap = document.querySelector(".toast-wrap");
  function toast(message, type) {
    if (!toastWrap) return;
    const el = document.createElement("div");
    el.className = "toast " + (type || "success");
    el.innerHTML = '<i class="fa-solid ' + (type === "error" ? "fa-circle-exclamation" : "fa-circle-check") + '"></i><span></span>';
    el.querySelector("span").textContent = message;
    toastWrap.appendChild(el);
    setTimeout(() => el.remove(), 6000);
  }
  window.unileapToast = toast;
  document.querySelectorAll(".toast[data-auto]").forEach((el) => setTimeout(() => el.remove(), 6000));

  // AJAX submission for enquiry / newsletter forms
  document.querySelectorAll("form[data-ajax]").forEach((form) => {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const button = form.querySelector("[type=submit]");
      const original = button ? button.innerHTML : "";
      form.querySelectorAll(".field-error").forEach((n) => n.remove());
      form.querySelectorAll(".invalid").forEach((n) => n.classList.remove("invalid"));
      if (button) { button.disabled = true; button.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending…'; }
      try {
        const res = await fetch(form.action, {
          method: "POST",
          body: new FormData(form),
          headers: { "X-Requested-With": "XMLHttpRequest" },
        });
        const data = await res.json();
        if (data.ok && data.redirect) {
          window.location.assign(data.redirect);
          return;
        } else if (data.ok) {
          form.reset();
          toast(data.message, "success");
        } else if (data.errors) {
          Object.entries(data.errors).forEach(([name, errs]) => {
            const input = form.querySelector('[name="' + name + '"]');
            const field = input && input.closest(".field");
            if (field) {
              field.classList.add("invalid");
              const msg = document.createElement("div");
              msg.className = "field-error";
              msg.textContent = errs[0];
              field.appendChild(msg);
            }
          });
          toast("Please check the highlighted fields.", "error");
        } else {
          toast(data.message || "Something went wrong.", "error");
        }
      } catch (err) {
        toast("Network error – please try again.", "error");
      } finally {
        if (button) { button.disabled = false; button.innerHTML = original; }
      }
    });
  });

  // Auto-submit filter forms when a checkbox / select changes
  document.querySelectorAll("form[data-autosubmit]").forEach((form) => {
    form.addEventListener("change", (e) => {
      if (e.target.matches("input[type=checkbox], select")) form.submit();
    });
  });

  // Search panel tabs (Home page): switch where the search goes instead of navigating away.
  document.querySelectorAll("[data-search-tab]").forEach((tab) => {
    tab.addEventListener("click", (e) => {
      const panel = tab.closest(".search-panel");
      const form = panel && panel.querySelector("[data-search-form]");
      if (!form) return;
      e.preventDefault();
      form.action = tab.getAttribute("href");
      panel.querySelectorAll("[data-search-tab]").forEach((t) => t.classList.toggle("active", t === tab));
    });
  });

  // Reveal on scroll
  const items = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) { entry.target.classList.add("in"); io.unobserve(entry.target); }
      });
    }, { threshold: 0.12 });
    items.forEach((el) => io.observe(el));
  } else {
    items.forEach((el) => el.classList.add("in"));
  }
})();
