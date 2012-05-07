# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from mongoengine import connect, fields, Document, EmbeddedDocument
from f5.models import ModelBase
# from pymongo.objectid import ObjectId

connect('meu_site_dev')


class Comment(EmbeddedDocument, ModelBase):
    id = fields.ObjectIdField(required=True)
    content = fields.StringField(max_length=1024, required=True)
    name = fields.StringField(max_length=120, required=True)
    email = fields.EmailField(required=True)
    date = fields.DateTimeField(default=datetime.now())


class Post(Document, ModelBase):
    title = fields.StringField(max_length=512, required=True)
    content = fields.StringField(required=True)
    pub_date = fields.DateTimeField(default=datetime.now())
    tags = fields.ListField(fields.StringField(max_length=30))
    comments = fields.ListField(fields.EmbeddedDocumentField(Comment))

    def __unicode__(self):
        return '"{title}" -> posted in {date}'.format(title=self.title,
            date=self.pub_date.strftime('%d/%m/%Y'))

#class Tag(Document):
#    tag_name = fields.StringField(unique=True, max_length=128, required=True)
#    count = fields.IntField(default=0)
