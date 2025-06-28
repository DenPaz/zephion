(function () {
  if (typeof Inputmask === "undefined") return;

  const masks = [
    {
      selector: ".phone-input",
      options: { mask: "(99) 9[9]999-9999", removeMaskOnSubmit: true },
    },
    {
      selector: ".date-input",
      options: {
        mask: "9999-99-99",
        removeMaskOnSubmit: true,
        placeholder: "yyyy-mm-dd",
      },
    },
  ];

  function initInputMasks(root = document) {
    if (!(root instanceof Element || root instanceof Document)) return;
    masks.forEach(({ selector, options }) => {
      root.querySelectorAll(selector).forEach((input) => {
        if (!input.inputmask) {
          Inputmask(options).mask(input);
        }
      });
    });
  }

  document.addEventListener("DOMContentLoaded", () => initInputMasks());
  document.addEventListener("htmx:afterSwap", (e) => initInputMasks(e.target));
  document.addEventListener("htmx:afterSettle", (e) =>
    initInputMasks(e.target)
  );
})();
