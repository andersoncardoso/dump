# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import datetime
#import pymongo
#from apps.main.models import ModelBase
#
#db = pymongo.Connection('localhost', 27017)['poll']
#
#class Poll(ModelBase):
#    collection = db.poll
#
#    def __init__(self, data=dict()):
#        self._fields = ['question', 'pub_date']
#        self.question = data.get('question', '')
#        self.pub_date = data.get('pub_date', datetime.datetime.now())
#
#    def __unicode__(self):
#        return self.question
#
#
#class Choice(ModelBase):
#    collection = db.choice
#
#    def __init__(self, data=dict()):
#        self._fields = ['poll', 'choice', 'votes']
#        self.poll = data.get('poll', None)
#        self.choice = data.get('choice', '')
#        self.votes = data.get('votes', 0)
#
#    def __unicode__(self):
#        return '[{}] - {}'.format(self.votes, self.choice)
from mongoengine import connect, Document
from mongoengine.fields import StringField, DateTimeField, IntField, ReferenceField

connect('poll')

class Poll(Document):
    question = StringField(required=True, max_length=80)
    pub_date = DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return self.question

class Choice(Document):
    poll = ReferenceField(Poll)
    choice = StringField(max_length=50)
    votes = IntField(default=0)

    def __unicode__(self):
        return '{choice} ({votes})'.format(choice=self.choice, votes=self.votes)
