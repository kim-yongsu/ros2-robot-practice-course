import {
  progressSummary,
  readProgress,
  resetProgress,
  setLessonCompletion,
} from "./course-progress-storage.js";

const SELECTORS = Object.freeze({
  anchor: "[data-course-progress-anchor]",
  markPanel: "[data-course-mark-complete]",
  markButton: "[data-mark-complete-button]",
  summary: "[data-course-progress-summary]",
  progressText: "[data-progress-text]",
  progressBar: "[data-progress-bar]",
  progressTrack: "[role='progressbar']",
  resetButton: "[data-course-progress-reset]",
  resumeLink: "[data-course-resume-link]",
  announcement: "[data-progress-announcement]",
});

const currentLesson = () => {
  const anchor = document.querySelector(SELECTORS.anchor);
  if (!anchor) {
    return null;
  }
  return {
    id: anchor.dataset.lessonId ?? "",
    title: anchor.dataset.lessonTitle ?? "",
    href: window.location.href,
  };
};

const announce = (message, scope = document) => {
  scope.querySelectorAll(SELECTORS.announcement).forEach((node) => {
    node.textContent = message;
  });
};

const updateSummary = (state) => {
  const summary = progressSummary(state);
  document.querySelectorAll(SELECTORS.summary).forEach((container) => {
    const text = container.querySelector(SELECTORS.progressText);
    const bar = container.querySelector(SELECTORS.progressBar);
    const track = container.querySelector(SELECTORS.progressTrack);
    if (text) {
      text.textContent = `${summary.completed} / ${summary.total} Lesson · ${summary.percent}%`;
    }
    if (bar) {
      bar.style.inlineSize = `${summary.percent}%`;
    }
    if (track) {
      track.setAttribute("aria-valuenow", String(summary.completed));
      track.setAttribute("aria-valuetext", `${summary.completed}개 Lesson 완료`);
    }
  });
};

const updateMarkButton = (state) => {
  const lesson = currentLesson();
  const panel = document.querySelector(SELECTORS.markPanel);
  const button = panel?.querySelector(SELECTORS.markButton);
  if (!lesson || !button) {
    return;
  }
  const completed = state.completed.includes(lesson.id);
  button.dataset.completed = String(completed);
  button.setAttribute("aria-pressed", String(completed));
  button.textContent = completed
    ? `Lesson ${lesson.id} 완료 표시 해제`
    : `Lesson ${lesson.id} 완료로 표시`;
  panel.classList.toggle("is-complete", completed);
};

const safeResumeHref = (lastLesson) => {
  if (!lastLesson?.href) {
    return null;
  }
  try {
    const target = new URL(lastLesson.href, window.location.href);
    if (target.origin !== window.location.origin) {
      return null;
    }
    return target.href;
  } catch (_error) {
    return null;
  }
};

const updateResumeLinks = (state) => {
  document.querySelectorAll(SELECTORS.resumeLink).forEach((link) => {
    const href = safeResumeHref(state.lastLesson);
    if (!href) {
      return;
    }
    link.href = href;
    link.textContent = `이어보기 · Lesson ${state.lastLesson.id}`;
    link.setAttribute("aria-label", `마지막 학습 이어보기: ${state.lastLesson.title}`);
  });
};

const render = (state = readProgress()) => {
  updateSummary(state);
  updateMarkButton(state);
  updateResumeLinks(state);
};

const bindCompletion = () => {
  const button = document.querySelector(SELECTORS.markButton);
  const lesson = currentLesson();
  if (!button || !lesson) {
    return;
  }
  button.addEventListener("click", () => {
    const state = readProgress();
    const next = !state.completed.includes(lesson.id);
    const updated = setLessonCompletion(lesson, next);
    announce(next ? `Lesson ${lesson.id} 완료를 저장했습니다.` : `Lesson ${lesson.id} 완료 표시를 해제했습니다.`);
    render(updated);
  });
};

const bindReset = () => {
  document.querySelectorAll(SELECTORS.resetButton).forEach((button) => {
    button.addEventListener("click", () => {
      const armed = button.dataset.resetArmed === "true";
      if (!armed) {
        button.dataset.resetArmed = "true";
        button.textContent = "한 번 더 눌러 초기화";
        announce("진행률을 초기화하려면 버튼을 한 번 더 누르세요.", button.parentElement ?? document);
        window.setTimeout(() => {
          button.dataset.resetArmed = "false";
          button.textContent = "진행률 초기화";
        }, 5000);
        return;
      }
      const state = resetProgress();
      button.dataset.resetArmed = "false";
      button.textContent = "진행률 초기화";
      announce("Burger 1권 진행률을 초기화했습니다.", button.parentElement ?? document);
      render(state);
    });
  });
};

const initialize = () => {
  bindCompletion();
  bindReset();
  render();
  window.addEventListener("storage", () => render());
  window.addEventListener("ros2-course-progress", (event) => render(event.detail));
};

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initialize, { once: true });
} else {
  initialize();
}
