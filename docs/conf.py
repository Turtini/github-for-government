from __future__ import annotations

project = "Turtini Docs"
author = "Turtini"
copyright = "Turtini"

# Sphinx extensions
extensions = [
    "myst_parser",
]

# Tell Sphinx we use Markdown
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# The root document (without file extension)
root_doc = "index"

# HTML theme
html_theme = "sphinx_rtd_theme"

# MyST configuration (safe, useful defaults)
myst_enable_extensions = [
    "colon_fence",   # ::: blocks
    "deflist",       # definition lists
    "tasklist",      # - [ ] checkboxes
    "attrs_inline",  # inline {#id .class}
]

# Optional: make external links open in new tab (nice for docs sites)
# html_theme_options = {"navigation_depth": 4}
