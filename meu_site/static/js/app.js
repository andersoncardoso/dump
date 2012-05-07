(function() {
  var blog, home, login, menuSetActive;
  var __indexOf = Array.prototype.indexOf || function(item) {
    for (var i = 0, l = this.length; i < l; i++) {
      if (this[i] === item) return i;
    }
    return -1;
  }, __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };
  $.fn.clearForm = function() {
    return this.each(function() {
      var tag, type;
      type = this.type;
      tag = this.tagName.toLowerCase();
      if (tag === 'form') {
        return $(':input', this).clearForm();
      }
      if (type === 'text' || type === 'password' || type === 'textarea') {
        return jQuery(this).val('');
      } else if (type === 'hidden') {
        return jQuery(this).val('');
      } else if (type === 'checkbox' || type === 'radio') {
        return jQuery(this).attr('checked', false);
      } else if (__indexOf.call('select', tag) >= 0) {
        return jQuery(this).val('');
      }
    });
  };
  menuSetActive = function(page) {
    var pages_index;
    page || (page = 'home');
    pages_index = {
      'home': 0,
      'blog': 1
    };
    return $("#main-menu li:eq(" + pages_index[page] + ")").addClass('active');
  };
  home = {
    init: function() {
      return true;
    }
  };
  login = {
    init: function() {
      this.browserid = $('#browserid');
      return this.browserid.click(__bind(function() {
        navigator.id.getVerifiedEmail(this.browseridEmailVerified);
        return false;
      }, this));
    },
    browseridEmailVerified: function(assertion) {
      if (assertion != null) {
        return $.ajax({
          type: 'POST',
          url: '/login/browserid/',
          data: {
            assertion: assertion
          },
          success: function(res, status, xhr) {
            if (res.success) {
              return window.location = '/';
            } else {
              return alert('login failure\nYou are not authorized!');
            }
          },
          error: function(res, status, xhr) {
            return alert("login failure " + res);
          }
        });
      } else {
        return alert("login failure!!!");
      }
    }
  };
  blog = {
    init: function() {
      this.btnPostDelete = $('#btnPostDelete');
      this.btnFormComment = $('#btnFormComment');
      this.formComment = $('#formComment');
      this.post_details = $('#post_details');
      this.post_comments_link = $('.post-comments-link');
      this.comment_section = $('#comment-section');
      this.comment_delete = $('.comment-delete');
      this.post_comments_link.click(__bind(function(evt) {
        var post_id;
        post_id = $(evt.target).attr('postID');
        return window.location = "/blog/post/details/" + post_id + "/";
      }, this));
      this.btnPostDelete.click(__bind(function(evt) {
        var element, pid;
        evt.preventDefault();
        element = $(evt.target);
        pid = element.attr('postID');
        if (confirm('Are you sure you want to delete this post?')) {
          return $.post("/blog/post/delete/", {
            id: pid
          }, __bind(function(data) {
            if (data.success === true) {
              return window.location = '/blog/';
            } else {
              return alert('error on deleting object');
            }
          }, this));
        }
      }, this));
      this.btnFormComment.click(__bind(function(evt) {
        var _id;
        evt.preventDefault();
        _id = this.post_details.attr('postID');
        this.formComment.find('#post_id').val(_id);
        return $.post('/blog/comment/create/', this.formComment.serialize(), __bind(function(data) {
          var f, field, msg, _i, _len, _ref, _results;
          _ref = this.formComment.find('.clearfix');
          for (_i = 0, _len = _ref.length; _i < _len; _i++) {
            field = _ref[_i];
            $(field).removeClass('error');
          }
          if (data.success) {
            this.formComment.clearForm();
            this.comment_section.prepend("<div class=\"comment well span14\" style=\"display: none;\">\n    <div class=\"comment-header\">\n        <span class=\"comment-header-name\">" + data.comment.name + "</span> &nbsp;said:\n        <span class=\"comment-header-date\">[ " + data.comment.date + " ]</span>\n    </div>\n    <p class=\"comment-comment\">\n        " + data.comment.content + "\n    </p>\n</div>");
            return this.comment_section.children().first().fadeIn('slow');
          } else {
            _results = [];
            for (field in data) {
              msg = data[field];
              f = this.formComment.find("#" + field);
              console.log(f);
              _results.push(this.formComment.find("#clearfix_" + field).addClass('error'));
            }
            return _results;
          }
        }, this), 'json');
      }, this));
      return this.comment_delete.click(__bind(function(evt) {
        var el, id;
        el = $(evt.target);
        id = el.attr('commentID');
        console.log("id is " + id);
        return $.post('/blog/comment/delete/', {
          id: id
        }, __bind(function(data) {
          if (data.success) {
            return location.reload();
          } else {
            return alert('error on deleting comment');
          }
        }, this), 'json');
      }, this));
    }
  };
  $(function() {
    var page, pages_selector;
    prettyPrint();
    page = location.pathname.split('/')[1];
    menuSetActive(page);
    pages_selector = {
      '': home,
      'login': login,
      'blog': blog
    };
    return pages_selector[page].init();
  });
}).call(this);
