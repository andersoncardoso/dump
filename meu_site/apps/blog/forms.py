# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import wtforms
from wtforms.validators import Required, Email
from f5.forms import Form
from blog.models import Post, Comment
from pymongo.objectid import ObjectId


class FormPost(Form):
    title = wtforms.TextField('Title', [Required()])
    content = wtforms.TextAreaField()
#    tags

    def save(self, id=None):
        p = Post.objects.with_id(id) if id else Post()
        p.title = self.title.data
        p.content = self.content.data
        p.save()
        return p


class FormComment(Form):
    name = wtforms.TextField('Name', [Required()])
    email = wtforms.TextField('Email', [Required(), Email()])
    content = wtforms.TextAreaField('Content', [Required()])
    post_id = wtforms.HiddenField('Post_id', [Required()])

    def save(self):
        comment = Comment(name=self.name.data,
                          email=self.email.data,
                          content=self.content.data)
        comment.id = ObjectId()
        Post.objects.with_id(self.post_id.data).update(push__comments=comment)
        return comment
