import os
import sys

sys.path.insert(0, os.path.abspath('../'))

project = 'fastemplate'
copyright = '2021, Henrique Brandao'
author = 'Henrique Brandao'

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "recommonmark"
]

source_suffix = ['.rst', '.md']

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
html_logo = '_static/logo.png'
html_favicon = html_logo
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
}
