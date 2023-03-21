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

#where your_cover.tex is your LaTeX file you want to be the cover.
#"maketitle": "\\input{your_cover.tex}"



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
        \vspace{-1.5in}

    ''',
}
