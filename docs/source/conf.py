"""Sphinx configuration for the ROS 2 robot practice course."""

project = "ROS 2 로봇 실습 강좌"
copyright = "2026, Kim Yongsu"
author = "Kim Yongsu"
release = "1.0.0-preview.2"
language = "ko"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
]

source_suffix = {".md": "markdown"}
master_doc = "index"
exclude_patterns = ["_build"]
nitpicky = True

myst_enable_extensions = [
    "attrs_inline",
    "colon_fence",
    "deflist",
    "linkify",
    "substitution",
]
myst_heading_anchors = 3

html_theme = "pydata_sphinx_theme"
html_title = "ROS 2 로봇 실습 강좌"
html_baseurl = "https://kim-yongsu.github.io/ros2-robot-practice-course/"
html_static_path = ["_static"]
html_css_files = ["css/course.css"]
html_js_files = [
    "js/course-theme-init.js",
    ("js/course-a11y.js", {"type": "module"}),
    ("js/course-progress.js", {"type": "module"}),
]
html_logo = "_static/img/course-mark.svg"
html_favicon = "_static/img/course-mark.svg"
html_show_sourcelink = False
html_last_updated_fmt = "%Y-%m-%d"

html_theme_options = {
    "navbar_align": "left",
    "header_links_before_dropdown": 4,
    "navigation_with_keys": True,
    "navigation_depth": 5,
    "show_nav_level": 2,
    "show_toc_level": 2,
    "show_prev_next": True,
    "back_to_top_button": True,
    "search_bar_text": "강좌에서 검색",
    "secondary_sidebar_items": ["page-toc"],
    "footer_start": ["copyright"],
    "footer_end": ["sphinx-version", "theme-version"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/kim-yongsu/ros2-robot-practice-course",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        }
    ],
}

copybutton_prompt_text = r"\$ |>>> "
copybutton_prompt_is_regexp = True
