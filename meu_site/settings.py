# -*- coding:utf-8 -*-
import os
import sys
here = os.path.abspath(os.path.dirname(__file__))

common = {
    'project_root': here,
    'host': '',
    'port': 8888,
    'debug': False,
    'template_path': os.path.join(here, 'templates'),
    'static_path': os.path.join(here, 'static'),
    'login_url': '/login/',
    'cookie_secret': '@#$%ˆ&FGHJKMNB$34567uJHgbnmjh$%ˆ&*fvb897ˆ&9879879n%ˆ&*(',
}


development = common.copy()
development.update({
    'port': 8888,
    'debug': True,
})


test = common.copy()
test.update({
    'port': 8080,
    'host': '0.0.0.0'
})


production = common.copy()
production.update({
    'port': 8000,
    'host': '127.0.0.1',
    'cookie_secret': 'change this on production',
})

if len(sys.argv) > 1:
    opt = {'development': development, 'test': test, 'production': production}
    settings = opt[sys.argv[1]]
else:
    settings = development
if len(sys.argv) > 2:
    host, port = sys.argv[2].split(':')
    settings.update({'host': host, 'port': port})
