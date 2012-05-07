# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from apps.poll.models import Poll, Choice
from lib.tornado_addons.route import route
from apps.main.handlers import BaseHandler
from forms import FormPoll

@route('/poll/add')
class PollAddHandler(BaseHandler):

    def get(self, *args, **kwargs):
        form = FormPoll()
        self.render('poll_add.html', form=form, xsrf=self.xsrf_form_html())

    def post(self, *args, **kwargs):
        self.check_xsrf_cookie()
        form = FormPoll(self.request.arguments)
        if form.validate():
            p = Poll()
            p.question = form.question.data
            p.save()
            for f in ['choice1', 'choice2', 'choice3']:
                if f in self.request.arguments:
                    c = Choice()
                    c.choice = getattr(form, f).data
                    c.poll = p
                    c.save()
            self.return_json({'success':True})
        else:
            d = {'success':False}
            d.update(form.errors)
            self.return_json(d)
