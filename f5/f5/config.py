# -*- coding: utf-8 -*- 
import os
import sys
import tornado.web
from tornado.options import define
from route import route

def run():
    tornado.ioloop.IOLoop.instance().start()

def F5_Application(settings=None):
    if settings:

        # for k, v in settings.iteritems():
        #     try:
        #         define(k, v) 
        #     except Exception as err:
        #         print '%s' % err

        apps_root = os.path.join(settings['project_root'], 'apps/')
        sys.path.append(apps_root)

        for app in os.listdir(apps_root):
            if os.path.isdir(os.path.join(apps_root, app)):
                 __import__('%s.handlers' % app, fromlist=[app])

        # application config
        application =  tornado.web.Application([
            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': settings['static_path']}),
            ] + route.get_routes(),
            **settings
        )


        application.listen(settings['port'], settings['host'])
        print('Starting server at {host}:{port}'.format(host=settings['host'], port=settings['port']))

        application.run = run

        return application
    
    
