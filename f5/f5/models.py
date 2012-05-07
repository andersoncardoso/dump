# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mongoengine import Document

class ModelBase():

    def to_dict(self):
        data = self._data.copy()
        data['id'] = data[None]
        del data[None]
        return data