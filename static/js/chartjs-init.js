(function () {
  if (typeof Chart === "undefined") return;

  function initCharts(root = document) {
    if (!(root instanceof Element || root instanceof Document)) return;

    root.querySelectorAll("[data-chartjs]").forEach((el) => {
      const wrapperId = el.dataset.chartjsWrapper;
      const configId = el.dataset.chartjs;

      const wrapper = root.querySelector(`#${wrapperId}`);
      const configScript = root.querySelector(`#${configId}`);

      if (!wrapper || !configScript) return;

      let chartConfig;
      try {
        chartConfig = JSON.parse(configScript.textContent);
      } catch (err) {
        console.error("Invalid chart config:", err);
        return;
      }

      wrapper.innerHTML = "";
      const canvas = document.createElement("canvas");
      wrapper.appendChild(canvas);
      const ctx = canvas.getContext("2d");

      chartConfig.options = chartConfig.options || {};
      chartConfig.options.responsive = true;
      chartConfig.options.animation = false;

      new Chart(ctx, chartConfig);
    });
  }

  document.addEventListener("DOMContentLoaded", () => initCharts());
  document.addEventListener("htmx:afterSwap", (e) => initCharts(e.target));
  document.addEventListener("htmx:afterSettle", (e) => initCharts(e.target));
})();
