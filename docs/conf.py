from __future__ import annotations
import os
import sys

# Make project root available to Sphinx
sys.path.insert(0, os.path.abspath(".."))

project = "GitHub for Government"
author = "Turtini"

extensions = [
    "myst_parser",
]

# We are using Markdown only
source_suffix = {
    ".md": "markdown",
}

# Tell Sphinx that our root document is README.md in the repo root
root_doc = "README"

# IMPORTANT: Tell Sphinx that source files live one level up (repo root)
# This allows you to keep all .md files in the root.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
    "attrs_inline",
]
