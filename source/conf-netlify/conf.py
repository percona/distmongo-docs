#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath("../"))
from conf import *
extensions.append('sphinx_gitstamp')
extensions.append('sphinx_copybutton')
html_theme = 'sphinx_material'
html_theme_options = {
    'base_url': 'http://bashtage.github.io/sphinx-material/',
    'repo_url': 'https://github.com/percona/distmongo-docs',
    'repo_name': 'percona/distmongo-docs',
    'color_accent': 'grey',
    'color_primary': 'orange',
    'globaltoc_collapse': True,
    'version_dropdown': True,
    'version_dropdown_text': 'Versions',
    'version_info': {
        "4.2": "https://docs.percona.com/percona-distribution-for-mongodb/4.2/",
        "4.4": "https://docs.percona.com/percona-distribution-for-mongodb/4.4/",
        "5.0": "https://docs.percona.com/percona-distribution-for-mongodb/5.0/",
        "Latest": "https://docs.percona.com/percona-distribution-for-mongodb/latest/"
    },
}
html_logo = '../_static/images/percona-logo.svg'
html_favicon = '../_static/images/percona_favicon.ico'
html_sidebars = {
        '**': ['localtoc.html', 'globaltoc.html', 'sourcelink.html', 'searchbox.html'],
        'using/windows': ['windowssidebar.html'],
}
pygments_style = 'emacs'
gitstamp_fmt = '%b %d, %Y'
copybutton_prompt_text = '$'
# Add any paths that contain templates here, relative to this directory.
templates_path = ['../_templates/theme']
# Path to custom css files. These will override the default css attribute if they exist
html_css_files = [
    '../_static/css/material.css',
]