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

from sphinx.ext import apidoc
import mock
import sys
import os

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
intersphinx_mapping = {
    'python': ('https://docs.python.org/3.8', None),
    'numpy': ("https://numpy.org/doc/stable/", None),
    'maplotlib': ('https://matplotlib.org', None),
    'pynn': ("http://neuralensemble.org/docs/PyNN/", None),
    'neo': (_READTHEDOCS_PATTERN.format('neo'), None),
    # We don't link to quantities; their docs are too shit
    # 'quantities': (_READTHEDOCS_PATTERN.format('python-quantities'), None),
    'spinn_utilities': (_READTHEDOCS_PATTERN.format('spinnutils'), None),
    'spinn_machine': (_READTHEDOCS_PATTERN.format('spinnmachine'), None),
    'spinnman': (_READTHEDOCS_PATTERN.format('spinnman'), None),
    'pacman': (_READTHEDOCS_PATTERN.format('pacman'), None),
    'data_specification': (
        _READTHEDOCS_PATTERN.format('dataspecification'), None),
    'spalloc': (_READTHEDOCS_PATTERN.format('spalloc'), None),
    'spinn_front_end_common': (
        _READTHEDOCS_PATTERN.format('spinnfrontendcommon'), None),
    'spynnaker': (_READTHEDOCS_PATTERN.format('spynnaker'), None),
    'spinnaker_graph_front_end': (
        _READTHEDOCS_PATTERN.format('spinnakergraphfrontend'), None)
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
project = u'SpiNNaker8Manchester'
copyright = u'2014-2021'
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '6.0'
# The full version, including alpha/beta/rc tags.
release = '6.0.1'

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
htmlhelp_basename = 'SpiNNaker8Manchesterdoc'

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
  ('index', 'SpiNNaker8Manchester.tex',
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
    ('index', 'SpiNNaker8Manchester', u'SpiNNaker 8 Manchester Documentation',
     [u''], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'SpiNNaker8Manchester', u'SpiNNaker 8 Manchester Documentation',
   u'', 'SpiNNaker8Manchester', '',
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
epub_title = u'SpiNNaker8 Manchester'
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

# The .py files (name beginning with a letter) we want in the doc build
wanted_files = {
    "spinn_utilities": [
        "abstract_base.py",
        "abstract_context_manager.py",
        "bytestring_utils.py",
        "classproperty.py",
        "conf_loader.py",
        "default_ordered_dict.py",
        "exceptions.py",
        "executable_finder.py",
        "find_max_success.py",
        "helpful_functions.py",
        "index_is_value.py",
        "log.py",
        "logger_utils.py",
        "ordered_set.py",
        "overrides.py",
        "package_loader.py",
        "ping.py",
        "progress_bar.py",
        "require_subclass.py",
        "safe_eval.py",
        "see.py",
        "socket_address.py",
        "timer.py",
        "make_tools/replacer.py",
        "testing/log_checker.py"],
    "spinn_machine": [
        "json_machine.py",
        "exceptions.py"],
    "spinnman": [
        "constants.py",
        "get_cores_in_run_state.py",
        "exceptions.py",
        "transceiver.py",
        "messages/multicast_message.py",
        "utilities/utility_functions.py",
        "utilities/appid_tracker.py",
        "utilities/locate_connected_machine_ip_address.py",
        "utilities/reports.py"],
    "pacman": [
        "exceptions.py",
        "model/partitioner_interfaces/abstract_slices_connect.py",
        "operations/algorithm_reports/reports.py",
        "operations/router_algorithms/routing_tree.py",
        "utilities/constants.py",
        "utilities/utility_calls.py",
        "utilities/json_utils.py",
        "utilities/algorithm_utilities/element_allocator_algorithm.py",
        "utilities/algorithm_utilities/machine_algorithm_utilities.py",
        "utilities/algorithm_utilities/routing_info_allocator_utilities.py",
        "utilities/algorithm_utilities/placer_algorithm_utilities.py",
        "utilities/algorithm_utilities/partition_algorithm_utilities.py"],
    "data_specification": [
        "constants.py",
        "utility_calls.py",
        "exceptions.py"],
    "spinn_front_end_common": [
        "interface/java_caller.py",
        "interface/abstract_spinnaker_base.py",
        "interface/simulator_state.py",
        "interface/config_handler.py",
        "utilities/class_utils.py",
        "utilities/constants.py",
        "utilities/system_control_logic.py",
        "utilities/globals_variables.py",
        "utilities/helpful_functions.py",
        "utilities/exceptions.py",
        "utilities/report_functions/energy_report.py"],
    "spynnaker": [
        "gsyn_tools.py",
        "spike_checker.py",
        "plot_utils.py",
        "pyNN/abstract_spinnaker_common.py",
        "pyNN/exceptions.py",
        "pyNN/spynnaker_simulator_interface.py",
        "pyNN/spynnaker_external_device_plugin_manager.py",
        "pyNN/models/abstract_pynn_model.py",
        "pyNN/models/projection.py",
        "pyNN/models/defaults.py",
        "pyNN/models/recorder.py",
        "pyNN/models/neuron/key_space_tracker.py",
        "pyNN/models/neuron/synaptic_matrices.py",
        "pyNN/models/neuron/master_pop_table.py",
        "pyNN/models/neuron/synaptic_matrix.py",
        "pyNN/models/neuron/synapse_io.py",
        "pyNN/models/neuron/synaptic_matrix_app.py",
        "pyNN/models/neuron/plasticity/stdp/common.py",
        "pyNN/models/spike_source/spike_source_array_vertex.py",
        "pyNN/models/spike_source/spike_source_poisson_vertex.py",
        "pyNN/models/spike_source/spike_source_poisson_machine_vertex.py",
        "pyNN/models/common/recording_utils.py",
        "pyNN/utilities/bit_field_utilities.py",
        "pyNN/utilities/spynnaker_failed_state.py",
        "pyNN/utilities/constants.py",
        "pyNN/utilities/data_cache.py",
        "pyNN/utilities/extracted_data.py",
        "pyNN/utilities/fake_HBP_Portal_machine_provider.py",
        "pyNN/utilities/running_stats.py",
        "pyNN/utilities/utility_calls.py",
        "pyNN/utilities/struct.py",
        "pyNN/utilities/variable_cache.py"],
    "spynnaker8": [
        "spynnaker8_simulator_interface.py",
        "spynnaker_plotting.py",
        "utilities/neo_convertor.py",
        "utilities/neo_compare.py"]
}


def _filtered_files(module_name, base):
    excludes = frozenset(
        os.path.join(base, e) for e in wanted_files.get(module_name, ()))
    for root, _dirs, files in os.walk(base):
        for filename in files:
            if filename.endswith(".py") and not filename.startswith("_"):
                full = os.path.join(root, filename)
                if excludes and full not in excludes:
                    yield full


def list_module(module_name, filters=None):
    if os.path.exists(module_name):
        for name in os.listdir(module_name):
            path = os.path.join(module_name, name)
            os.remove(path)
    else:
        os.mkdir(module_name)
    source = os.path.dirname(__import__(module_name).__file__)
    if not filters:
        filters = _filtered_files(module_name, source)
    apidoc.main(['-o', module_name, source, *filters])


list_module("spinn_utilities")
list_module("spinn_machine")
list_module("spinnman")
list_module("pacman")
list_module("data_specification")
list_module("spinn_front_end_common")
list_module("spynnaker")
list_module("spynnaker8")
