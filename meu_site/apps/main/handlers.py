# -*- coding: utf-8 -*-
import os
import urllib
import tornado.web
import tornado.auth
import tornado.httpclient
import tornado.escape
from settings import settings
from markdown import markdown
from f5.route import route
from f5.handlers import BaseHandler


@route('/', name='index')
class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        f = os.path.join(settings['template_path'], 'content/index.md')
        with open(f) as f_:
            index_md = markdown(f_.read())
        self.render('index.html', index_md=index_md, context=self.get_context())


@route('/login/?', name='login')
class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')


@route('/login/google/?', name='login_google')
class GoogleLoginHandler(BaseHandler, tornado.auth.GoogleMixin):
    authorized_users = ['apierre.cardoso@gmail.com']  # TODO put this on settings

    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        if self.get_argument("openid.mode", None):
            self.get_authenticated_user(self.async_callback(self._on_auth))
            return
        self.authenticate_redirect()

    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, "Google auth failed")
        else:
            if user['email'] in self.authorized_users:
                self.set_secure_cookie('user', tornado.escape.json_encode(user))
                self.redirect('/')
            else:
                self.redirect('/logout/')


@route('/logout/?', name='logout')
class LogoutHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie('user')
        self.redirect('/')


 ## ---- initial browser id integration
@route('/login/browserid/?', name='login_browserid')
class BrowserIDAuthLoginHandler(BaseHandler):
    authorized_users = ['apierre.cardoso@gmail.com']   # TODO put this on settings

    @tornado.web.asynchronous
    def post(self):
        assertion = self.get_argument('assertion')
        http_client = tornado.httpclient.AsyncHTTPClient()
        domain = self.request.host
        print 'HOSt: ', domain
        url = 'https://browserid.org/verify'
        data = {
          'assertion': assertion,
          'audience': domain,
        }
        http_client.fetch(
            url,
            method='POST',
            body=urllib.urlencode(data),
            callback=self.async_callback(self._on_response)
        )

    def _on_response(self, response):
        struct = tornado.escape.json_decode(response.body)
        if struct['status'] != 'okay':
            raise tornado.web.HTTPError(400, "Failed assertion test")
        email = struct['email']
        if email in self.authorized_users:
            user = {'first_name': 'Anderson', 'email': email}
            self.set_secure_cookie('user', tornado.escape.json_encode(user))
            self.return_json({'success': True})
        else:
            self.return_json({'success': False})
