Dispenser
=========

Dispenser inspires to be a project management tool, create a skeleton, manage metadata, help with tests.

INACTIVE
--------

Dispenser is out of my reach for now, despite people liking the idea, 
I won't be able to finish the project (not now anyway). Thanks for your suppoert, 
if someone wants to take it and make their own, feel free!

Goal
----

Graphical interface for python project management. NOT AN IDE. Just a tool to easily - with few clicks
generate project structure and few relatively static files and keep those up to date, more below.

Needs to be fully integrated with OS and take care of it's dependencies (git, virtualenv, pip).
This means it's going to be much harder for windows - possibly impossible.

Should be able to open an existing project and find compatible stuff, offer the rest

Plugins plugins plugins! Don't want bloated core. And letting others do what I'd do is cool. No but seriously, stay lightweight, few kB, everything should be EASY.
Plugins however should be INTEGRATED IN THE APP, ONE CLICK INSTALL (and uninstall)! 
Provide templating for the files - one default, people can choose custom and have setup.py look different

Brief overview
--------------

- Easily start and setup python project - keep it up to date across all the files
    - setup.py
    - tests/
    - docs/
    - virtualenv(s) and environmental variables manager
    - git (with ignore) - not a git gui, just generate and ability to manage .gitignore file, maybe connect tag to version management
    - metadata (not only pypi metadata, but also version, author, copyright, license, changelogs)
    - readme
    - sphinx
    - dependencies management - checker for new versions, compatibility warnings based on their dependencies
        - keep dependencies separate for: consumer, testing, development
    - sdist, bdist, twine
    - Coverage, Test checker
    - Button to start a shell in the project (with virtualenv active)

- Support for plugins to implement various CI, testing methods, layouts, etc.
    - .travis.yml
    - .codeclimate.yml
    - autoenv (actually maybe have this in core, linux plebs should know how awesome it is)

- Possible support for 'export' plugins - check compatibility based on dependencies? Is it possible? No experience.
    - Heroku
    - Windows
    - Apt, Yum and other unix package managers
    - OS X
    - Android
    - iOS
    - bat, make, bash? Who knows. That's why plugins

Graphical User Interface
------------------------

Toga will be used - uses native stuff of the OS, yay!

DEVELOPMENT
-----------

Open to everybody, license gonna be MIT, feedback and issues contribution/discussion is just as valuable as programming itself.

NOTES
-----

Possibly Test Driven Development. Should be fun, easy and possible to create functional tests - I want to do that! Just call function with some params and
parse the resulting file. FUN.
