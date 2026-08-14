const SELECTORS = Object.freeze({
  main: "main, .bd-main .bd-content",
  searchInput: "input[type='search'], .search-button__button, [aria-label*='검색']",
  header: ".bd-header, header",
});

const ensureMainTarget = () => {
  const main = document.querySelector(SELECTORS.main);
  if (main && !main.id) {
    main.id = "main-content";
  }
  return main;
};

const ensureSkipLink = () => {
  const main = ensureMainTarget();
  if (!main || document.querySelector(".course-skip-link")) {
    return;
  }
  const link = document.createElement("a");
  link.className = "course-skip-link";
  link.href = `#${main.id}`;
  link.textContent = "본문으로 건너뛰기";
  if (!main.hasAttribute("tabindex")) {
    main.setAttribute("tabindex", "-1");
  }
  link.addEventListener("click", () => {
    window.requestAnimationFrame(() => main.focus({ preventScroll: true }));
  });
  document.body.prepend(link);
};

const focusSearch = () => {
  const candidate = document.querySelector(SELECTORS.searchInput);
  if (candidate instanceof HTMLElement) {
    candidate.focus();
    if (candidate instanceof HTMLButtonElement) {
      candidate.click();
    }
  }
};

const bindKeyboardSearch = () => {
  document.addEventListener("keydown", (event) => {
    const target = event.target;
    const editing = target instanceof HTMLInputElement
      || target instanceof HTMLTextAreaElement
      || target instanceof HTMLSelectElement
      || target?.isContentEditable;
    if (event.key === "/" && !editing && !event.metaKey && !event.ctrlKey && !event.altKey) {
      event.preventDefault();
      focusSearch();
    }
  });
};

const setScrollPadding = () => {
  const header = document.querySelector(SELECTORS.header);
  const height = header instanceof HTMLElement ? header.getBoundingClientRect().height : 0;
  document.documentElement.style.setProperty("--measured-header-offset", `${Math.ceil(height + 16)}px`);
};

const labelThemeTreeToggles = () => {
  document.querySelectorAll("details > summary").forEach((summary) => {
    if (summary.textContent.trim() || summary.hasAttribute("aria-label")) {
      return;
    }
    const item = summary.closest("li");
    const label = item?.querySelector(":scope > a")?.textContent?.trim() || "하위 목차";
    summary.setAttribute("aria-label", `${label} 펼치기`);
  });
};

const initialize = () => {
  ensureSkipLink();
  bindKeyboardSearch();
  setScrollPadding();
  labelThemeTreeToggles();
  window.addEventListener("resize", setScrollPadding, { passive: true });
};

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initialize, { once: true });
} else {
  initialize();
}
