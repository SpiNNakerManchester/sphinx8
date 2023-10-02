# -*- coding: utf-8 -*-
#
# data_allocation documentation build configuration file, created by
# sphinx-quickstart on Tue Jun 17 08:56:46 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
# See note at the bottom regarding this
# os.environ['SPHINX_APIDOC_OPTIONS'] = \
#    "members,undoc-members,inherited-members,noindex"
from sphinx.ext import apidoc


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

_on_rtd = os.environ.get('READTHEDOCS', 'False') == 'True'

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
]

_READTHEDOCS_PATTERN = 'https://{}.readthedocs.io/en/latest/'
spinnaker_doc_version = "7.1.0"

intersphinx_mapping = {
    'python': ('https://docs.python.org/3.8', None),
    'numpy': ("https://numpy.org/doc/stable/", None),
    'maplotlib': ('https://matplotlib.org', None),
    'pynn': ("http://neuralensemble.org/docs/PyNN/", None),
    'neo': (_READTHEDOCS_PATTERN.format('neo'), None),
    # We don't link to quantities; their docs are too shit
    # 'quantities': (_READTHEDOCS_PATTERN.format('python-quantities'), None),
    # We don't link to quantities; their docs are too awful
    'spinn_utilities': (
        f'https://spinnutils.readthedocs.io/en/{spinnaker_doc_version}/',
        None),
    'spinn_machine': (
        f'https://spinnmachine.readthedocs.io/en/{spinnaker_doc_version}/',
        None),
    'spinnman': (
        f'https://spinnman.readthedocs.io/en/{spinnaker_doc_version}/', None),
    'pacman': (
        f'https://pacman.readthedocs.io/en/{spinnaker_doc_version}/', None),
   'spinn_front_end_common': (
        'https://spinnfrontendcommon.readthedocs.io/en/'
        f'{spinnaker_doc_version}/', None),
    'spalloc_client': (
        'https://spalloc_client.readthedocs.io/en/'
        f'{spinnaker_doc_version}/', None),
    'spynnaker': (
        f'https://spynnaker.readthedocs.io/en/{spinnaker_doc_version}/', None),
    'spinnaker_graph_front_end': (
        'https://spinnakergraphfrontend.readthedocs.io/en/'
        f'{spinnaker_doc_version}/', None)
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'SpiNNakerManchester'
copyright = u'2014'
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1!7.1'
# The full version, including alpha/beta/rc tags.
release = '1!7.1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'SpiNNakerManchesterdoc'

# Where to get the mathjax javascript library from because the default is
# horribly outdated in some versions of Sphinx.
mathjax_path = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'SpiNNakerManchester.tex',
   u'SpiNNaker 8 Manchester Documentation', u'', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'SpiNNakerManchester', u'SpiNNaker Manchester Documentation',
     [u''], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'SpiNNakerManchester', u'SpiNNaker Manchester Documentation',
   u'', 'SpiNNakerManchester', '',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'SpiNNaker Manchester'
epub_author = u''
epub_publisher = u''
epub_copyright = u'2017'

# The basename for the epub file. It defaults to the project name.
# epub_basename = u'data_allocation'

# The HTML theme for the epub output.
# Since the default themes are not optimized
# for small screen space, using the same theme for HTML and epub output is
# usually not wise. This defaults to 'epub', a theme designed to save visual
# space.
# epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
# epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
# epub_identifier = ''

# A unique identification for the text.
# epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
# epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
# epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
# epub_tocdepth = 3

# Allow duplicate toc entries.
# epub_tocdup = True

# Choose between 'default' and 'includehidden'.
# epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
# epub_fix_images = False

# Scale large images.
# epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# epub_show_urls = 'inline'

# If false, no index is generated.
# epub_use_index = True

autoclass_content = 'both'

# We want to document __call__ when encountered
autodoc_default_options = {
    "members": None,
    "special-members": "__call__"
}

if _on_rtd:
    # Some packages need mocking
    autodoc_mock_imports = [
        '_tkinter', 'scipy', 'scipy.stats', 'matplotlib',
        'pyNN', 'pyNN.random', 'pyNN.common', 'neo', 'quantities', 'lazyarray']


# See not at the bottom
def excluded_because_in_init(module_name, base):
    for root, _dirs, files in os.walk(base):
        if "__init__.py" in files:
            init = os.path.join(root,  "__init__.py")
            with open(init) as f:
                for line in f:
                    if line.startswith("from ."):
                        parts = line.split()
                        yield os.path.join(root, parts[1][1:]+".py")
    # if module_name == "spynnaker":
    #    yield os.path.join(
    #        base, "pyNN", "external_devices", "__init__.py")


def list_module(module_name):
    if os.path.exists(module_name):
        for name in os.listdir(module_name):
            path = os.path.join(module_name, name)
            os.remove(path)
    else:
        os.mkdir(module_name)
    source = os.path.dirname(__import__(module_name).__file__)
    filters = excluded_because_in_init(module_name, source)
    apidoc.main(['-o', module_name, source, *filters])


list_module("spinn_utilities")
list_module("spinn_machine")
list_module("spinnman")
list_module("pacman")
list_module("data_specification")
list_module("spinn_front_end_common")
list_module("spynnaker")
list_module("spinnaker_graph_front_end")

# See not at the bottom
# add noindex to semantic sugar init files
semantic_sugar_files = [
    os.path.join("spynnaker", "spynnaker.pyNN.rst"),
    os.path.join("spynnaker", "spynnaker.pyNN.external_devices.rst"),
    os.path.join("spynnaker", "spynnaker.pyNN.extra_models.rst"),
    os.path.join("spinnaker_graph_front_end", "spinnaker_graph_front_end.rst")
]
for semantic_sugar_file in semantic_sugar_files:
    with open(semantic_sugar_file, 'r') as f:
        for line in f:
            pass
        noindex_line = line.replace("show-inheritance","noindex")
    with open(semantic_sugar_file, "a",  encoding="utf-8") as f:
        f.write(noindex_line)

"""
Notes to explain some of the hacks here.

The issue is that a many classes can be imported multiple ways 
as they are exposed by _init.py

for example: ACSource
spynnaker.pyNN.models.current_sources.ac_source.ACSource
spynnaker.pyNN.models.current_sources.ACSource
spynnaker.pyNN.ACSource

The import from its directory init is standard practice so we want to keep it
The import from spynnaker.pyNN is to allow easy calls in user scripts

This causes Sphinx and especially ReadTheDocs to create multiple copies of
the documentation.  That is ok
But it also cause confusion as to which to link to.

The current fix is in two parts.

1. Find all the local files imported by init files looking for the from .
pattern and excluding them.

note: This assumes all local import use the from . format!

note: A another approach which is nicer if kept up to date was used in
release 1!6.0.0,  This kept an list of the files exposed via init.
This was done for in the local doc and here.
Experience however showed that the list was not kept up to date

2. For the semantic sugar init files can be told to not be used by adding 
a noindex flags
Note: This must be done here and also in the local conf.py files.
(or at least if there are any links using an exposed class)
note2: the individual conf.py run in a different directory to the global ones.

note: it is easy to add the noindex to all of the files and in theory this 
should remove the need for the excluded files
This is done using 
os.environ['SPHINX_APIDOC_OPTIONS'] = \
    "members,undoc-members,inherited-members,noindex"
before importing apidoc

Last time this approach was tried it generated a lot of weird errors especially
from spinn_utilities.configs.camel_case_config_parser or the configparser
it depends on

Another approach tried was to exclude the __init__.py files.
This fails because Sphinx assumes that only directories
(after removing excludes) which contain an init files contain code.
It only worked for directories with an init but no other py files.

3. There are two ways to configure readthedocs. 
Using their websites Advance Settings pages or a .readthedocs.yaml file.
The second approach is the one recommended and this was done in version 1!6.0.0
Experience however showed that the files fell behind and stopped working as 
expected so they where removed and the simple website gui is used.
In particular the Install your project using setup.py was not happening.

4. the reason the semantic_sugar_file no_index work has to read the last line
of the file and then replace and write it back is because sphinx/readthedocs
is inconsistent in the number of characters it places before the 
show-inheritance and the noindex has to have the same number of spaces.
This inconistancy was observed between different local and global runs 
"""