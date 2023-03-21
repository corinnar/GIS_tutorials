# Configuration file for the Sphinx documentation builder.

# -- Project information

project =  'MAPPING TO SUPPORT REDD+ PLANNING AND SECURE MULTIPLE BENEFITS: TOOLBOX AND TUTORIALS FOR QGIS AND ARCGIS'



release = '0.1'
version = '0.1.0'

today_fmt = '%B %d, %Y' 
author = 'UNEP-WCMC'
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

# -- General configuration

latex_elements = {
     'classoptions': ',oneside',
    
# The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper', 

# The font size ('10pt', '11pt' or '12pt').
    'pointsize': '11pt',

# Additional stuff for the LaTeX preamble.
    'preamble': r'''
        \usepackage{charter}
        \usepackage[sfdefault]{roboto}
        \usepackage{inconsolata}
    ''',
}
