# conf.py (repo root)

project = "GitHub for Government"
author = "Turtini"

extensions = ["myst_parser"]

source_suffix = {
    ".md": "markdown",
}

root_doc = "index"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
    "attrs_inline",
]

html_logo = "_static/turtini-logo.png"  # or .svg
html_static_path = ["_static"]

html_css_files = [
    "turtini.css",
]

html_js_files = [
    "turtini-banner.js",
]

html_theme_options = {
    # Collapses left nav nicely
    "collapse_navigation": False,
    "navigation_depth": 4,
}

# Show last updated date
html_last_updated_fmt = "%B %d, %Y"

templates_path = ["docs/_templates"]
html_last_updated_fmt = "%B %d, %Y"

from datetime import datetime

html_context = {
    "turtini_year": datetime.utcnow().year,
}
