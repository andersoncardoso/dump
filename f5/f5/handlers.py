# -*- coding: utf-8 -*-
import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    def return_json(self, data_dict):
        """
        acessory method to return json objects
        """
        self.set_header('Content-Type', 'application/json')
        json_ = tornado.escape.json_encode(data_dict)
        self.write(json_)
        self.finish()

    def get_current_user(self):
        user_json = self.get_secure_cookie('user')
        if user_json:
            return tornado.escape.json_decode(user_json)
        else:
            return None

    def get_context(self):
        context = type('', (), {}) #dynamic object for holding context references
        context.user = self.get_current_user()
        return context