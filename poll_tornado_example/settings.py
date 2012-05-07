import os

ROOT = os.path.abspath(os.path.dirname(__file__))
port = 8888
debug = True
template_path = os.path.join(ROOT, 'templates')
static_path = os.path.join(ROOT, 'static')

APPS = [
    'poll',
    'main', ]

