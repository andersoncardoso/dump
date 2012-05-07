# -*- coding:utf-8 -*-

import wtforms
from wtforms.validators import Required
from apps.main.forms import Form

class FormPoll(Form):
    question = wtforms.TextField(u'Questão', [Required(message='Por favor, preencha esse campo.')])
    choice1 = wtforms.TextField(u'1a Escolha')
    choice2 = wtforms.TextField(u'2a Escolha')
    choice3 = wtforms.TextField(u'3a Escolha')