# Configuration file for the Sphinx documentation builder.

# -- Project information

project =  'MAPPING TO SUPPORT REDD+ PLANNING AND SECURE MULTIPLE BENEFITS: TOOLBOX AND TUTORIALS FOR QGIS AND ARCGIS'
author = '© UNEP, 2023 ................. Author: UNEP-WCMC'
copyright = '© UNEP, 2023'

release = 'Beta 0.1'
version = '0.1.0'

today_fmt = '%B %d, %Y' 

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.autosectionlabel'
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
#html_theme_path = ['_themes']

# Add this to the top of the conf.py file
import os
import sys
sys.path.insert(0, os.path.abspath('C:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\arcgispro-py3'))
import sphinx_rtd_theme


# -- Options for HTML output
extensions = [
    'sphinx_rtd_theme',
]

html_theme = 'sphinx_rtd_theme'

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]



# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- General configuration

latex_elements = {
     'classoptions': ',oneside',
    
# The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper', 

# The font size ('10pt', '11pt' or '12pt').
    'pointsize': '12t',

    
# Additional stuff for the LaTeX preamble.
    'preamble': r'''
        \usepackage{charter}
        \usepackage[sfdefault]{roboto}
        \usepackage{inconsolata}
        \usepackage[english]{babel}
        \usepackage{tocloft}
        \addto\captionsenglish{\renewcommand\contentsname{Table of Contents}}
        \renewcommand{\cfttoctitlefont}{\hfill\Large\bfseries}
        \renewcommand{\cftaftertoctitle}{\hfill\normalsize}

    ''',
}
