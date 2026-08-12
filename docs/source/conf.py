"""Sphinx configuration for the ROS 2 robot practice course."""

project = "ROS 2 로봇 실습 강좌"
copyright = "2026, Kim Yongsu"
author = "Kim Yongsu"
release = "1.0.0-preview.1"
language = "ko"

extensions = ["myst_parser", "sphinx_copybutton"]
source_suffix = {".md": "markdown"}
master_doc = "index"
exclude_patterns = ["_build"]
html_theme = "furo"
html_title = "ROS 2 로봇 실습 강좌"
html_static_path = ["_static"]
html_css_files = ["course.css"]
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "linkify",
    "substitution",
]
copybutton_prompt_text = r"\$ |>>> "
copybutton_prompt_is_regexp = True
nitpicky = True
