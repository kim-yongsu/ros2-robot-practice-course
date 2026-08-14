import AxeBuilder from "@axe-core/playwright";
import { expect, test } from "@playwright/test";

const URLS = Object.freeze({
  home: "/index.html",
  volume: "/courses/burger/volume-1/index.html",
  start: "/courses/burger/volume-1/start.html",
  readingGuide: "/courses/burger/volume-1/reading-guide.html",
  learningMap: "/courses/burger/volume-1/learning-map.html",
  part: "/courses/burger/volume-1/part-01-environment/index.html",
  lesson: "/courses/burger/volume-1/chapters/01-burger로-ros-2의-공통-기준선을-만든다.html",
  troubleshooting: "/courses/burger/volume-1/troubleshooting.html",
  exercises: "/courses/burger/volume-1/exercises.html",
});

const expectNoHorizontalOverflow = async (page) => {
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  expect(overflow).toBeLessThanOrEqual(1);
};

const expectNoSeriousAxeViolations = async (page) => {
  const results = await new AxeBuilder({ page }).analyze();
  const blocking = results.violations.filter((item) => ["critical", "serious"].includes(item.impact));
  expect(blocking, JSON.stringify(blocking, null, 2)).toEqual([]);
};

test("home exposes the first CTA and six-PART route", async ({ page }) => {
  await page.goto(URLS.home);
  await expect(page.getByRole("link", { name: "Burger 1권 시작하기" })).toBeVisible();
  await expect(page.locator(".roadmap-card")).toHaveCount(6);
  await expectNoHorizontalOverflow(page);
  await expectNoSeriousAxeViolations(page);
});

test("volume landing exposes progress, requirements, and nested PARTs", async ({ page }) => {
  await page.goto(URLS.volume);
  await expect(page.getByRole("heading", { name: "환경 기준선에서 재현 가능한 프로젝트까지" })).toBeVisible();
  await expect(page.getByRole("progressbar")).toHaveAttribute("aria-valuemax", "25");
  await expect(page.locator(".part-card")).toHaveCount(6);
  await expectNoHorizontalOverflow(page);
});

test("lesson exposes execution, verdict, STOP, evidence, and next learning", async ({ page }) => {
  await page.goto(URLS.lesson);
  for (const heading of ["학습 목표", "실행", "PASS / HOLD / FAIL", "STOP 조건", "증거 체크리스트", "다음 단원"]) {
    await expect(page.getByRole("heading", { name: heading, exact: true })).toBeVisible();
  }
  const complete = page.getByRole("button", { name: /Lesson 01 완료로 표시/ });
  await complete.click();
  await expect(page.locator("[data-mark-complete-button]")).toHaveAttribute("aria-pressed", "true");
  await page.goto(URLS.volume);
  await expect(page.locator("[data-progress-text]")).toContainText("1 / 25");
  await expectNoSeriousAxeViolations(page);
});

test("progress storage ignores damaged and unknown lesson data", async ({ page }) => {
  await page.goto(URLS.volume);
  await page.evaluate(() => {
    const noisyCompleted = Array.from({ length: 40 }, (_, index) => String(index + 1).padStart(2, "0"));
    window.localStorage.setItem(
      "ros2-course:burger:v1:progress",
      JSON.stringify({
        version: 1,
        completed: ["01", "01", "x", ...noisyCompleted],
        lastLesson: {
          id: "99",
          title: "Unknown",
          href: "/bad.html",
        },
        updatedAt: "2026-08-14T00:00:00.000Z",
      }),
    );
  });
  await page.reload();
  await expect(page.locator("[data-progress-text]")).toContainText("25 / 25");
  await expect(page.locator("[data-course-resume-link]")).not.toHaveAttribute("href", /bad\.html/);
});

test("keyboard focus reaches the primary learning action", async ({ page }) => {
  await page.goto(URLS.home);
  await page.keyboard.press("Tab");
  const skip = page.locator(".course-skip-link");
  await expect(skip).toBeFocused();
  await page.keyboard.press("Enter");
  await expect(page.locator("#main-content")).toBeFocused();
});

test("PART landing remains usable without hover", async ({ page }) => {
  await page.goto(URLS.part);
  await expect(page.locator(".lesson-card")).toHaveCount(4);
  await expect(page.getByRole("link", { name: "학습하기" }).first()).toBeVisible();
  await expectNoHorizontalOverflow(page);
});

test("course pages use one consistent learning navigation", async ({ page }) => {
  for (const url of [
    URLS.volume,
    URLS.start,
    URLS.readingGuide,
    URLS.learningMap,
    URLS.part,
    URLS.lesson,
    URLS.troubleshooting,
    URLS.exercises,
  ]) {
    await page.goto(url);
    await expect(page.locator(".lesson-prev-next")).toHaveCount(1);
    await expect(page.locator(".prev-next-footer, .prev-page, .next-page")).toHaveCount(0);
  }
});
