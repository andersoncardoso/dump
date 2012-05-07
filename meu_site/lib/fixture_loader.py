# -*- coding: utf-8 -*-
import os
import codecs
from datetime import datetime
import sys
sys.path.append('../')
from apps.blog.models import Post

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

fixture = eval(codecs.open(os.path.join(project_root, 'templates/content/new_blog_fixture.json'), 'r', encoding='utf-8').read())
for obj in fixture:
    post = Post(
        title=unicode(obj['title'], 'utf-8'),
        content=unicode(obj['content'], 'utf-8'),
        pub_date=datetime.strptime(obj['pub_date'], '%Y-%m-%d %H:%M:%S')
    )
    post.save(safe=True)
    print 'added %s' % obj['title']
