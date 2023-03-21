# Configuration file for the Sphinx documentation builder.

# -- Project information


project = 'GIS tutorials'
author = 'Corinna Ravilious'

release = '0.1'
version = '0.1.0'

today_fmt = '%d %m %y'

# -- General configuration

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
    'papersize': 'letterpaper',

# The font size ('12pt', '13pt' or '14pt').
    'pointsize': '13pt',


    
# Additional stuff for the LaTeX preamble.
    'preamble': r'''
        \enwffont{Roboto-LF}{Roboto}
        \enwffont{RobotoCondensed-LF}{Roboto Condensed}
        \enwffont{RobotoSlab-LF}{Roboto Slab}
    ''',
}

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

#html_theme = 'sphinx_rtd_theme'




# -- Options for EPUB output
epub_show_urls = 'footnote'

latex_elements = {
  'extraclassoptions': 'openany,oneside'
}
