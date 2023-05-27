# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'APPFL'
copyright = '2021, Argonne National Laboratory'
author = 'Argonne National Laboratory'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.napoleon',
        'sphinx.ext.viewcode',
        'sphinx.ext.autosummary',
        'sphinx.ext.todo',
        'sphinx.ext.doctest',
        'sphinx.ext.intersphinx',
        'sphinx.ext.coverage',
        'sphinx.ext.mathjax',
        'sphinx.ext.ifconfig',
        'sphinx.ext.autosectionlabel',
        'myst_parser',
        'sphinx_rtd_theme',
        'nbsphinx',
]

autodoc_mock_imports = [
        "torch",
        "omegaconf",
        "grpc",
        "numpy",
        "mpi4py",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_data']

nbsphinx_execute = 'never'
