import sphinx
import python_docs_theme

project = 'py_everything'
copyright = '2021, PyBash'
author = 'PyBash'

release = '2.0.0'

extensions = ['sphinx.ext.autodoc', 'python_docs_theme']

templates_path = ['_templates']

exclude_patterns = []

html_theme = 'python_docs_theme'

html_static_path = ['_static']

html_logo = '..\\..\\extra\\logo.png'

html_favicon = '..\\..\\extra\\logo.png'
