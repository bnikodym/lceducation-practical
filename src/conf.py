import sys
import os
import sphinx_bootstrap_theme

sys.path.append(os.path.abspath('../exts'))

# -- Curriculum Site Settings ------------------------------------------------

# Customize for the specific site. Any options in the html_theme_options
# dictionary below may be overriden here
site_theme_options = {
    'navbar_title': '',
    'navbar_site_name': "Pages",
    'bootswatch_theme': 'launchcode',
}

project = 'Introduction to Professional Web Development in JavaScript'

# -- Project information -----------------------------------------------------


copyright = '2019, LaunchCode'
author = 'LaunchCode'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
    'external_links',
    'admonition_icons',
    'replit',
    'ordered_toctree',
]

replit_user = 'launchcode'

# numfig:
numfig_number_figures = True
numfig_figure_caption_prefix = "Figure"

# disable smart quotes
smartquotes = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['./_templates']

# The suffix(es) of source filenames.
source_suffix = ['.rst']

highlight_language = 'none'
html_show_copyright = False
html_show_sphinx = False
html_copy_source = False

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'docs']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'fruity'


# -- Options for HTML output -------------------------------------------------

# The theme, via sphinx_bootstrap_theme
html_theme = 'bootstrap'

# sphinx_bootstrap_theme must be installed locally
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# The logo that will appear in the navbar, relative to _static
html_logo = '_static/images/logos/lc-ed-logo.png'

# Theme-specific options
default_theme_options = {
    # Navigation bar title
    'navbar_title': 'Site',

    # Tab name for entire site. (Default: "Site")
    'navbar_site_name': "Pages",

    # A list of tuples containing pages or urls to link to.
    # Valid tuples should be in the following forms:
    #    (name, page)                 # a link to a page
    #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
    #    (name, "http://example.com", True) # arbitrary absolute url
    # Note the "1" or "True" value above as the third argument to indicate
    # an arbitrary url.
    'navbar_links': [
    ],

    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': False,

    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': False,

    # Tab name for the current pages TOC. (Default: "Page")
    'navbar_pagenav_name': "Contents",

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 1,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "false",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "true",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "",

    'bootswatch_theme': "launchcode",
    'bootstrap_version': "3",
    'html_logo_alt_text': 'LaunchCode logo',
}

html_theme_options = {**default_theme_options, **site_theme_options}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = {
    '**': []
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'CurriculumModuledoc'

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


def setup(app):
    app.add_stylesheet('fa/css/all.css')
    app.add_stylesheet('css/launchcode.css')
    app.add_stylesheet('css/site.css')
    app.add_config_value('recommonmark_config', {
            'enable_eval_rst': True,
            }, True)
    app.add_transform(AutoStructify)
