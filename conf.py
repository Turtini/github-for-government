# conf.py (repo root)

project = "GitHub for Government"
author = "Turtini"

extensions = ["myst_parser"]

source_suffix = {
    ".md": "markdown",
}

root_doc = "README"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
    "attrs_inline",
]
