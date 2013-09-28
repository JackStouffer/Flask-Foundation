#Flask Foundation
[![Build Status](https://travis-ci.org/JackStouffer/Flask-Foundation.png)](https://travis-ci.org/JackStouffer/Flask-Foundation)

Flask Foundation is a solid foundation for flask applications, built with best practices, that you can easily construct your website/webapp off of.

Built off of the [bootstrapy project](https://github.com/kirang89/bootstrapy)

Best practices were learned from [Creating Websites With Flask](http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/) and [Getting Bigger With Flask](http://maximebf.com/blog/2012/11/getting-bigger-with-flask/), and most importantly [Larger Applications With Flask](http://flask.pocoo.org/docs/patterns/packages/).

##What Is Included

* Best Practices setup with blueprints and SQLAlchemy models that will allow you to grow cleanly
* A helpful makefile
* An awesome management script
* [Bootstrap](http://getbootstrap.com/) is included but easily replaceable
* [Typeplate](http://typeplate.com/): some nice typographic defaults, also easily replaceable
* [py.test](http://pytest.org/latest/) tests
* [Sphinx](http://sphinx-doc.org/): Helps you create some awesome docs for your users, or your internal team
* [Flask-Assets](http://flask-assets.readthedocs.org/en/latest/): A library that packages css and js files and applies filters to them like the closure complier
* [Flask-Cache](http://pythonhosted.org/Flask-Cache/): A simple library that adds the ability to cache specified views
* [Flask-SQLAlchemy](http://pythonhosted.org/Flask-SQLAlchemy/): Flask integration with SQLAlchemy
* [Flask-Script](http://flask-script.readthedocs.org/en/latest/): Allows one to create awesome management scripts
* [Flask-WTF](https://flask-wtf.readthedocs.org/en/latest/index.html): Integrates WTForms into flask

##What Is Not Included

* A WSGI setup. This is largely based off of ones individual production setup, so it is not included.
* A Redis or a Memcached setup for Flask-Cache.
* A database migration tool, like South. This is not included due to the fact that for 99.9% of people this is overkill.
* A database backend for SQLAlchemy. SQLAlchemy does not come with a way to connect to the database and must be provided. These backends can be found on the SQLAlchemy documentation.
* A admin interface tool. Some like the library Flask-Admin, others want to build their own. I don't include it because I believe that it is no where close to being as customizable as it should be.
* A publishing tool like fabric. Which tool you use is totally up to your personal preference as well as your production environment, which is why it is not included.
* A vagrant setup. For most people vagrant is overkill, but the vagrant setup is entirely based of off your production setup so it is not included here.

##Usage

###The Makefile

First, lets use the included make file to setup our dev environment. To see all of the available commands, just type make.

    $ make

    env         create a development environment using virtualenv
    deps        install dependencies
    clean       remove unwanted stuff
    lint        check style with flake8
    test        run all your tests using py.test

If you are ever confused about what each command does, take a look at the makefile, it is very straight forward.

So to setup the dev environment, let's type 

    $ make env

This will install virtualenv if you don't have it and setup a local python instance. Then it installs all of the needed libs from the requirements.txt file. Now we have our setup with all of the needed 3rd party libs.

Tests are done through py.test, and reside in the tests directory. To run the tests, just type 

    $ make test

You can check you PEP8 compliance by typing 

    $ make lint

Documentation for your project can be created with Sphinx in the docs directory. For more information, refer to the [Sphinx documentation](http://sphinx-doc.org/).

###The Management File

Simply type

    ./manage.py

and you will get a list of commands that you can use to manage the project. For example, to run the server, use 

    ./manage.py server 

and if the installation when well, you should have a working server on http://localhost:5000

This management script was created with Flask-Script and is fairly easy to add your own commands, simply refer to their [docs](http://flask-script.readthedocs.org/en/latest/).

###The Flask Application Structure

Before going to far into this, you should at least skim the documentation of all of the thrid party libraries listed above so you have a better understanding of what is going on here.

The flask application itself lives in the appname directory. Obviously, you change this to the name of your application. Once you do though, you must go through and fix all of the imports where it uses the appname name. The easiest way to find them all is to type

    grep -R appname *

To make things organized, this project is in a pseudo MVC setup. With the controllers as flask blueprints, the models as SQLAlchemy models, and the views as the templates.

The main logic of the application is in the \_\_init\_\_.py. This is done so that the application is treated as a module by python which helps later when importing things. Here, we setup all of the third party libs and load in our configuration in an application factory, which is a function that creates and returns an instance of our application. This is done for easier testing purposes and modularity. The function create\_app takes the path of the config file that you want to use and the type of environment that the server is running in. Most of the library initialization is self explanatory, but let me explain the configuration loading. In your shell's startup script (if you are using bash, its .bash_profile), you must enter this line:

    APPNAME_ENV = 'dev' or APPNAME_ENV='prod'

This tells the application which class, located in settings.py, to load in for the configuration. To see the different configs, take a look at the settings.py file. This is explained more in depth in the flask docs [here](http://flask.pocoo.org/docs/config/#development-production).

After everything is initialized, the application loads in the main blueprint from the controllers file. If you don't know how flask blueprints work, check out [this](http://flask.pocoo.org/docs/blueprints/) page in the flask documentation. The controllers/main.py file is where we have our current example logic, with a homepage and a example WTForms page. 

WTForm classes are held in a separate file called forms.py and imported when needed.

The templates are stored in the templates directory for the main blueprint. It is encouraged, but not required, that every new blueprint has its own templates directory inside of the main templates directory. Blueprints have a special variable to make this easy:

    simple_page = Blueprint('simple_page', __name__, template_folder='simple')

and now when you have a function 

    @simple_page.route('/')
    def function()
        return render_template('index.html')

it will return simple/index.html

As you can see, the example code uses bootstrap. You are quite able to rip it out and use your own framework if you wish. 

All of the templates inherit from the base.html template to avoid repeating yourself and to avoid discrepancies between pages. Also, as you can see in base.html, it is encouraged that you make use of Flask-Assets when ever possible. Using this to your advantage will dramatically speed up load times.

The models in this application are SQLAlchemy models in the models.py file, an example User model has been provided.

If you are still confused about how this project is structured, I encourage you to read the blog posts listed at the top of the README file.

Lets talk about the tests. All of the tests are in the test_appname.py file, and the tests are run with py.test. Nothing is to fancy in the first test class, but in the next one we see some special initialization with the database, this is due to flask not actually running and Flask-SQLAlechmy not being initialized properly. Also, we see here the use of app.test\_client(), which means we can use functions to send GET and POST requests from our tests. This is how we test our forms and if the urls are returning correctly.

##Production
First off, it is very, very important that if you ever open source a flask application based upon this, to not include the settings.py file in your repo. Obviously, your database password is in it, but your secret key as well, which is used to cryptographically sign all of flask's session data.

When going into production there are several things that you should do. First, look at your options for deploying on an actual server [here](http://flask.pocoo.org/docs/deploying/). Using the flask development server is NOT recommended for production for several good reasons. Deploying to the server manually is tedious, so you might want to look into deploying with [fabric](http://flask.pocoo.org/docs/patterns/fabric/) or [distributee](http://flask.pocoo.org/docs/patterns/distribute/#distribute-deployment). This isn't php, so logging errors doesn't come out of the box, [here](http://flask.pocoo.org/docs/errorhandling/) is a great resource on the subject. Also, there are several awesome plug-ins available for flask, they can be found on the flask website [here](http://flask.pocoo.org/extensions/), or just searching "flask" on github.

##Licenses
The original bootstrapy project and the added code from this project are licensed under the BSD license.
