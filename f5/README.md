# What is F5?

is an micro-framework/boilerplate for working with Tornado web server.
It focus on speed, but on a easy way. Uses:

* mongodb as primary DB.
* mongoengine as ODM.
* wtforms, for django-like form handling

Its intended runtime is pypy, but you can obviously run on cpython.

# features (intended):

* django-like form handling
* django-like models
* routing
* easy bottle/flask-like handlers
* authentication
* scaffolds
* pagination
* logging
* easy configuration


# setting up an app ... 

settings.py:
<pre>
# -*- coding:utf-8 -*-
import os
here = os.path.abspath(os.path.dirname(__file__))

development = {
	'project_root' : here,
	'port' : 8888,
	'debug' : True,
	'template_path' : os.path.join(here, 'templates'),
	'static_path' : os.path.join(here, 'static'),
	'login_url' : '/login/',
	'cookie_secret' : 'some_giant_and_weird_string_here!',
}
test = {
	# teste settings	
	# ... 
}
production = {
	# production settings 
	# ...
}

settings = development
</pre>

myapp.py
<pre>
from settings import settings
from lib.f5.config import F5_Application

def main():
    application = F5_Application(settings)
    # start server
    application.run()

if __name__ == '__main__':
    main()
</pre>

# Usage: 

...