(function () {
  if (typeof flatpickr === "undefined") return;

  function initFlatpickrs(root = document) {
    if (!(root instanceof Element || root instanceof Document)) return;
    root.querySelectorAll("[data-flatpickr]").forEach((input) => {
      const config = input.dataset.flatpickr
        ? JSON.parse(input.dataset.flatpickr)
        : {};
      flatpickr(input, config);
    });
  }

  document.addEventListener("DOMContentLoaded", () => initFlatpickrs());
  document.addEventListener("htmx:afterSwap", (e) => initFlatpickrs(e.target));
  document.addEventListener("htmx:afterSettle", (e) =>
    initFlatpickrs(e.target)
  );
})();
