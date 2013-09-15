Flask Foundation
================

Flask Foundation is a solid foundation for flask applications, built with best practices, that you can easily construct your website/webapp off of.

Built off of the [bootstrapy project](https://github.com/kirang89/bootstrapy)

What Is Included
----------------

* Best Practices setup with blueprints and SQLAlchemy models that will allow you to grow
* A helpful makefile
* An awesome management script
* Bootstrap is included but easily replaceable
* Some nice typographic defaults, also easily replaceable
* Tests through nose
* Sphinx: Helps you create some awesome docs for your users, or your internal team
* Flask-DebugToolbar: A helpful toolbar that is enabled when debug = true. Based of django debugtoolbar
* Flask-Assets: A library that packages css and js files and applies filter to them like the closure complier
* Flask-Cache: A simple library that adds the ability to cache specified views
* Flask-SQLAlchemy: A flask integration with SQLAlchemy
* Flask-Script: Allows one to create awesome management scripts
* Flask-WTF: Integrates WTForms into flask

The make file is included to help with common tasks

```
env         create a development environment using virtualenv
deps        install dependencies
clean       remove unwanted stuff
lint        check style with flake8
test        run all your tests using nose
```

So for example, if I wanted to check my app for PEP8 errors, I would type

```
make lint
```

Licenses
--------

The original bootstrapy project is licensed under the BSD license, The added code of Flask Foundation is under the MIT license. 