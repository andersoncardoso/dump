import tornado.ioloop
import tornado.web
from tornado.options import options, define
import settings
from lib.tornado_addons.route import route

[__import__('apps.%s.handlers' % app, fromlist=['apps.%s' % app]) for app in settings.APPS]

def main():
    define('port', default=settings.port)
    define('debug', default=settings.debug)
    define('template_path', default=settings.template_path)
    define('static_path', default=settings.static_path)

    app_settings = dict(
        port=options.port,
        debug=options.debug,
        template_path=options.template_path
    )

    # application config
    application = tornado.web.Application([
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': options.static_path}),
        ] + route.get_routes(),
        **app_settings
    )
    
    # start server
    print('Starting server at localhost:{port}'.format(port=options.port))
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()