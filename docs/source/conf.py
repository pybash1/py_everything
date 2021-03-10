import sphinx
import sphinx_rtd_theme


project = 'py_everything'
copyright = '2021, Play 4 Tutorials'
author = 'Play 4 Tutorials'

release = '1.1.1'

extensions = ['sphinx.ext.autodoc', 'sphinx_rtd_theme']

templates_path = ['_templates']

exclude_patterns = []

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'navigation_depth': 2,
}

html_static_path = ['_static']
