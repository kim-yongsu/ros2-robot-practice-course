const STORAGE_KEY = "ros2-course:burger:v1:progress";
const TOTAL_LESSONS = 25;
const LESSON_IDS = new Set(Array.from({ length: TOTAL_LESSONS }, (_, index) => String(index + 1).padStart(2, "0")));

const createEmptyState = () => ({
  version: 1,
  completed: [],
  lastLesson: null,
  updatedAt: null,
});

const normalizeLessonId = (lessonId) => String(lessonId ?? "").padStart(2, "0");

const isAllowedLessonId = (lessonId) => LESSON_IDS.has(normalizeLessonId(lessonId));

const isValidLastLesson = (value) => (
  value
  && typeof value === "object"
  && typeof value.id === "string"
  && isAllowedLessonId(value.id)
  && typeof value.title === "string"
  && typeof value.href === "string"
);

const normalizeState = (value) => {
  if (!value || typeof value !== "object") {
    return createEmptyState();
  }
  const completed = Array.isArray(value.completed)
    ? [...new Set(value.completed.map(normalizeLessonId))]
        .filter(isAllowedLessonId)
        .sort()
    : [];
  return {
    version: 1,
    completed,
    lastLesson: isValidLastLesson(value.lastLesson) ? value.lastLesson : null,
    updatedAt: typeof value.updatedAt === "string" ? value.updatedAt : null,
  };
};

export const readProgress = () => {
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    return raw ? normalizeState(JSON.parse(raw)) : createEmptyState();
  } catch (error) {
    console.warn("강좌 진행률을 읽지 못했습니다.", error);
    return createEmptyState();
  }
};

export const writeProgress = (state) => {
  const normalized = normalizeState({
    ...state,
    updatedAt: new Date().toISOString(),
  });
  try {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(normalized));
  } catch (error) {
    console.warn("강좌 진행률을 저장하지 못했습니다.", error);
  }
  window.dispatchEvent(new CustomEvent("ros2-course-progress", { detail: normalized }));
  return normalized;
};

export const setLessonCompletion = (lesson, completed) => {
  const state = readProgress();
  const id = normalizeLessonId(lesson.id);
  if (!isAllowedLessonId(id)) {
    return writeProgress(state);
  }
  const values = new Set(state.completed);
  if (completed) {
    values.add(id);
  } else {
    values.delete(id);
  }
  return writeProgress({
    ...state,
    completed: [...values].sort(),
    lastLesson: {
      id,
      title: String(lesson.title ?? `Lesson ${id}`),
      href: String(lesson.href ?? ""),
    },
  });
};

export const resetProgress = () => writeProgress(createEmptyState());

export const progressSummary = (state = readProgress()) => ({
  completed: state.completed.length,
  total: TOTAL_LESSONS,
  percent: Math.round((state.completed.length / TOTAL_LESSONS) * 100),
});

export { STORAGE_KEY, TOTAL_LESSONS };
