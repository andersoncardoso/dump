# -*- coding: utf-8 -*-
from datetime import datetime
from tornado.escape import xhtml_escape
from tornado.web import authenticated
from blog.forms import FormPost, FormComment
from blog.models import Post
from f5.handlers import BaseHandler
from f5.route import route
from f5.pagination import Paginator
from markdown import markdown
from pymongo.objectid import ObjectId


@route('/blog/?', name='blog')
class BlogIndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        _posts = Post.objects.order_by('-pub_date')
        offset = self.get_argument('offset', 10)
        page = self.get_argument('page', 1)

        if _posts:
            _page = Paginator(_posts, offset).page(page)
            posts = _page.object_list
            has_next = _page.has_next()
            has_previous = _page.has_previous()
        else:
            posts = []
            has_next = False
            has_previous = False

        _data = dict(posts=posts, page=int(page), has_next=has_next, has_previous=has_previous,
                     markdown=markdown, context=self.get_context())
        self.render('blog_index.html', **_data)


@route('/blog/post/create/?$', name='post_add')
class PostCreateHandler(BaseHandler):

    @authenticated
    def get(self, *args, **kwargs):
        form = FormPost()
        _data = dict(form=form, xsrf=self.xsrf_form_html(), post_id=None, form_action='/blog/post/create/',
                     context=self.get_context())
        self.render('blog_post_form.html', **_data)

    @authenticated
    def post(self, *args, **kwargs):
        self.check_xsrf_cookie()
        form = FormPost(self.request.arguments)
        if form.validate():
            form.save()
            # self.return_json({'success':True})
            self.redirect('/blog/')
        else:
            d = {'success': False}
            d.update(form.errors)
            self.return_json(d)


@route('/blog/post/details/(?P<pid>\w+)/?$', name="post_details")
class PostDetailsHandler(BaseHandler):
    def get(self, pid, *args, **kwargs):
        post = Post.objects.with_id(pid)
        form = FormComment()
        _data = dict(post=post, xsrf=self.xsrf_form_html(), form=form, form_action='/blog/comment/create/',
                     escape=xhtml_escape, markdown=markdown, context=self.get_context())
        self.render('blog_post.html', **_data)


@route('/blog/post/update/(?P<pid>\w+/?$)', name='post_update')
class PostUpdateHandler(BaseHandler):
    @authenticated
    def get(self, pid, *args, **kwargs):
        post = Post.objects.with_id(pid)
        form = FormPost(**post.to_dict())

        _data = dict(form=form, xsrf=self.xsrf_form_html(), form_action='/blog/post/update/{pid}'.format(pid=pid),
                     post_id=pid, context=self.get_context())
        self.render('blog_post_form.html', **_data)

    @authenticated
    def post(self, pid, *args, **kwargs):
        self.check_xsrf_cookie()
        form = FormPost(self.request.arguments)
        if form.validate():
            form.save(id=pid)

            # self.return_json({'success':True})
            self.redirect('/blog/post/details/%s' % pid)
        else:
            d = {'success': False}
            d.update(form.errors)
            self.return_json(d)


@route('/blog/post/delete/?$', name='blog_post_delete')
class PostDeleteHandler(BaseHandler):
    @authenticated
    def post(self):
        try:
            pid = self.get_argument('id')
            post = Post.objects.with_id(pid)
            post.delete(safe=True)
            self.return_json({'success': True, 'id': pid})
        except Exception as err:
            print 'err: %s' % err
            self.return_json(dict(success=False))


@route('/blog/comment/create/?$', name='blog_comment_create')
class CommentCreateHandler(BaseHandler):
    def post(self, *args, **kwargs):
        self.check_xsrf_cookie()
        form = FormComment(self.request.arguments)
        if form.validate():
            comment = form.save()
            self.return_json({
                'success': True,
                'comment': {
                    'name': comment.name,
                    'content': comment.content,
                    'date': datetime.now().strftime('%Y-%m-%d %H:%M')
                }
            })
            # self.redirect('/blog/')
        else:
            d = {'success': False}
            d.update(form.errors)
            self.return_json(d)


@route('/blog/comment/delete/?$')
class CommentDeleteHandler(BaseHandler):
    @authenticated
    def post(self, *args, **kwargs):
        try:
            comment_id = self.get_argument('id')
            post = Post.objects.get(comments__id=comment_id)

            for index, c in enumerate(post.comments):
                if c.id == ObjectId(comment_id):
                    comment_index = index
                    break
            if comment_index:
                post.comments.pop(comment_index)
                post.save()

            self.return_json({'success': True, 'id': comment_id})
        except Exception as err:
            print 'err: %s' % err
            self.return_json(dict(success=False))
