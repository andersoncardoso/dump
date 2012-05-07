import tornado.web
import tornado.auth
import tornado.escape
from apps.poll.forms import FormPoll
from lib.tornado_addons.route import route
from apps.poll.models import Poll, Choice

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        pass
#        self.db = pymongo.Connection('localhost', 27017, )['poll']

    def return_json(self, data_dict):
        """
        acessory method to return json objects
        """
        self.set_header('Content-Type', 'application/json')
        json_ = tornado.escape.json_encode(data_dict)
        self.write(json_)
        self.finish()


@route('/', name='index')
class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        form = FormPoll()
        xsrf = self.xsrf_form_html()
        polls = []
        for p in Poll.objects:
            polls.append((p, Choice.objects(poll=p)))
        self.render("index.html", polls=polls, xsrf=xsrf, form=form)


@route('/login/?', name='login')
class LoginHandler(BaseHandler, tornado.auth.GoogleMixin):
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
            self.render("logged.html", user=user)
