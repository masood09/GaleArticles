[![Build Status](https://travis-ci.org/masood09/GaleArticles.svg?branch=master)](https://travis-ci.org/masood09/GaleArticles)
[![Coverage Status](https://coveralls.io/repos/github/masood09/GaleArticles/badge.svg?branch=master)](https://coveralls.io/github/masood09/GaleArticles?branch=master)

# GaleArticles

# Introduction

GaleArticles is a simple Django based application. The frontend is written using Vue.js. This application only does limited things. Display a list of articles, view the complete article and search the articles. As a bonus some randomness is thrown around!!

# Issues

GaleArticles was written in a very short period of time, literally in few hours. Although it has been tested on many different Python versions, database engines and Django versions, I would recommend you have the latest version of Python, Django and other dependencies to avoid any nasty surprises.

# Prerequisites

The following are the software requirements to run GaleArticles.

* Python version 2.7, 3.4 or 3.5 (3.5 preferred)
* Django version 1.8 or 1.9 (1.9 preferred)
* Ruby (latest version)
* Nodejs (latest version)
* git (latest version)

# Installation

The documentation is written from OS X/Linux user perspective. Most of the commands should work on a Windows box, but I give no guarantee. Please google or drop me an email if you are stuck.

The recommended way of installing this application (for that matter any Django/Python application) is by using virtualenv Python package. The advantage of this approach is that we can isolate the Python development environment (packages, settings etc.,) on a per project. The installation is pretty simple.

```bash
pip install virtualenv
```

Once virtualenv is installed, you should create an virtual environment. The below command will create a new virtual called django_env

 ```bash
 virtualenv django_env
 ```

 To activate the envirnoment use the below command

 ```bash
 source ./django_env/bin/activate
 ```

The next step would be to clone this repository! Yay finally!

```bash
git clone https://github.com/masood09/GaleArticles.git
```

To install all the dependencies for this project, execute the following command from the GaleArticles directory

```bash
pip install -r requirements/development.txt
```

To complete the installation of this project (and to enjoy the beautiful fixtures that I have created), please follow the below instructions

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata fixtures.json
```

To build the frontend assets, follow the instructions to build the frontend build toolchain.

```bash
gem install --no-ri --no-rdoc sass
npm install
npm run build
```

To test the application and gather coverage information execute the following commands

```bash
coverage run manage.py test
coverage html
```

Phew!!

Now we are ready to fire up the server and see how the application looks

```
cd ..
python manage.py runserver
```

Open your browser and point it to [http://127.0.0.1:8000](http://127.0.0.1:8000)


# Overriding the settings

You can over-ride any settings of the application by creating **local_settings.py** file in Gale/config file. Any settings defined thier would over-ride the settings specified in settings.py file.
