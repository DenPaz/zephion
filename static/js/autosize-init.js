(function () {
  if (typeof autosize === "undefined") return;

  function initAutosize(root = document) {
    const elements = root.querySelectorAll('[data-kt-autosize="true"]');
    if (!elements.length) return;
    autosize.destroy(elements);
    autosize(elements);
  }

  document.addEventListener("DOMContentLoaded", () => initAutosize());
  document.addEventListener("htmx:afterSwap", (e) => initAutosize(e.target));
  document.addEventListener("htmx:afterSettle", (e) => initAutosize(e.target));
  document.addEventListener("shown.bs.modal", (e) => {
    initAutosize(e.target);
  });
})();
