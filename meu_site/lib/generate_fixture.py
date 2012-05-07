# -*- coding: utf-8 -*-
import os
import codecs
from datetime import datetime
import sys
sys.path.append('../')
from apps.blog.models import Post

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with codecs.open(os.path.join(project_root, 'templates/content/new_blog_fixture.json'), 'w', encoding='utf-8') as fixture:
    fixture.write('[')
    for obj in Post.objects:
        fixture.write('''
        { "title": "%s",
          "content": """%s""",
          "pub_date": "%s"
        },
        ''' % (
            obj['title'],
            obj['content'],
            obj['pub_date'].strftime('%Y-%m-%d %H:%M:%S'))
        )
    fixture.write(']')
