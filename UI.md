# First Window - project selector

* List of projects previously opened/created by Dispenser
* Button to create new
* Button to load a project

# Create New project

* Form with:
    * Author information
    * Desired Python version
    * pytest/unittest/nose etc.
    * License
    * Keywords
    * Short description
    * Project location
    * URL
    * Stuff based on plugins, suggest plugins
    * Template choice

-> redirects to project management window

# Load a project

* Location prompt
    * Enable remote via ssh

-> redirects to project management window

# Project management

* Status bar with
    * status of tests
    * test coverage
    * Version number
    * License
    * Documentation status?
    * Dependencies compatibility (scan their dependencies, make sure no clashes)
* List of dependencies next to available newest version
* List of supported python versions
* Button that opens shell/gui at project path
* Button run tests
* Button for test settings
* Button to release a new version
* Button to edit metadata
* Button for plugin management

# Release a new version

* Checklist - Deployment method
    * Pypi
    * Heroku
    * Other various possible deployment methods
* New version prompt (provide guidelines to versioning semantic, possible easymode with just 'major/minor/bugfix release'
* Changelog prompt

# Test settings

* Periodic check frequency
* Default button run quiet (for statusbar)/verbose (open shell, let user debug)

# Edit metadata

* Pretty much the same as generate

# Plugin management

* List of installed plugins
* Button to explore more (browser redirect)
