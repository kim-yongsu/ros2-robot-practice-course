(function () {
  const validModes = new Set(["auto", "light", "dark"]);
  let mode = document.documentElement.dataset.theme || "";
  try {
    mode = window.localStorage.getItem("mode") || window.localStorage.getItem("theme") || mode;
  } catch (_error) {
    mode = mode || "auto";
  }
  if (!validModes.has(mode)) {
    mode = "auto";
    try {
      window.localStorage.setItem("mode", mode);
      window.localStorage.setItem("theme", mode);
    } catch (_error) {
      // Ignore storage failures; the data attribute still gives the theme script a valid mode.
    }
  }
  document.documentElement.dataset.mode = mode;
  document.documentElement.dataset.theme = mode;
}());
