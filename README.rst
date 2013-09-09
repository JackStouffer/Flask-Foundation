==========
bootstrapy
==========

A bootstrap application that takes away the pain of setting up a python application for production and lets you focus on coding instead.

Usage
-----
::

    #Sets up environment and installs dependencies
    $ make env

    #Activate the environment
    $ . env/bin/activate

    #Shows the list of commands available
    $ make help

      env         create a development environment using virtualenv
      deps        install dependencies
      clean       remove unwanted stuff
      lint        check style with flake8
      test        run all your tests using nose
      production  run test suite and do a release
      release     package and upload a release
      sdist       package

Setup Notes
-----------

* In order to be able to generate PDF and PS files from reStructuredText using LaTeX on Debian-based systems you need to install the following software:

    ``sudo apt-get install wget build-essential python2.5-dev texlive-full``

* Use `webhooks`_ to update docs at `Read The Docs`_ whenever you make a commit to your project.

.. _webhooks: https://read-the-docs.readthedocs.org/en/latest/webhooks.html
.. _Read The Docs: https://readthedocs.org/

License
-------

bootstrapy is BSD licensed, so feel free to use it as you like.

