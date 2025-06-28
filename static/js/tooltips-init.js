(function () {
  if (typeof bootstrap === "undefined") return;

  function initTooltips(root = document) {
    if (!(root instanceof Element || root instanceof Document)) return;
    root.querySelectorAll('[data-bs-toggle="tooltip"]').forEach((element) => {
      bootstrap.Tooltip.getOrCreateInstance(element);
    });
  }

  document.addEventListener("DOMContentLoaded", () => initTooltips());
  document.addEventListener("htmx:afterSwap", (e) => initTooltips(e.target));
  document.addEventListener("htmx:afterSettle", (e) => initTooltips(e.target));
})();
