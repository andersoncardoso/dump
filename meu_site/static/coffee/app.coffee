#
#  UTILS
$.fn.clearForm = ->
    this.each ->
        type = this.type
        tag = this.tagName.toLowerCase()
        if tag is 'form'
            return $(':input',this).clearForm()
        if type in ['text', 'password', 'textarea']
            jQuery(this).val ''
        else if type is 'hidden' #&& this.name !== "csrfmiddlewaretoken"){
            jQuery(this).val ''
        else if type in ['checkbox', 'radio']
            jQuery(this).attr 'checked', false
        else if tag in 'select'
            jQuery(this).val ''

# Menu set active (main nav bar)
menuSetActive = (page)->
    page or= 'home'
    pages_index =
        'home' : 0
        'blog' : 1
    $("#main-menu li:eq(#{pages_index[page]})").addClass 'active'

home =
    init : ->
        true

login =
    init : ->
        @browserid = $('#browserid')

        @browserid.click =>
            navigator.id.getVerifiedEmail @browseridEmailVerified
            false

    browseridEmailVerified : (assertion) ->
        if assertion?
            $.ajax
                type: 'POST'
                url: '/login/browserid/'
                data: { assertion: assertion }
                success: (res, status, xhr) ->
                    if res.success
                        window.location = '/'
                    else
                        alert 'login failure\nYou are not authorized!'
                error: (res, status, xhr) ->
                    alert "login failure #{res}"
        else
            alert "login failure!!!"

blog =
    init : ->
        @btnPostDelete = $('#btnPostDelete')
        @btnFormComment = $('#btnFormComment')
        @formComment = $('#formComment')
        @post_details = $('#post_details')
        @post_comments_link = $('.post-comments-link')
        @comment_section = $('#comment-section')
        @comment_delete = $('.comment-delete')

        @post_comments_link.click (evt) =>
            post_id = $(evt.target).attr('postID')
            window.location = "/blog/post/details/#{post_id}/"

        @btnPostDelete.click (evt) =>
            evt.preventDefault()
            element = $(evt.target)
            pid =  element.attr 'postID'
            if confirm 'Are you sure you want to delete this post?'
                $.post "/blog/post/delete/", {id : pid }, (data) =>
                    if data.success is true
                        window.location = '/blog/'
                    else
                        alert 'error on deleting object'

        @btnFormComment.click (evt) =>
            evt.preventDefault()
            _id = @post_details.attr('postID')
            @formComment.find('#post_id').val(_id)
            $.post '/blog/comment/create/',
                @formComment.serialize()
                (data) =>
                    $(field).removeClass 'error' for field in @formComment.find('.clearfix')
                    if data.success
                        @formComment.clearForm()
                        @comment_section.prepend """
                        <div class="comment well span14" style="display: none;">
                            <div class="comment-header">
                                <span class="comment-header-name">#{data.comment.name}</span> &nbsp;said:
                                <span class="comment-header-date">[ #{data.comment.date} ]</span>
                            </div>
                            <p class="comment-comment">
                                #{data.comment.content}
                            </p>
                        </div>
                        """
                        @comment_section.children().first().fadeIn 'slow'
                    else
                        for field, msg of data
                            f = @formComment.find("##{field}")
                            console.log f
                            @formComment.find("#clearfix_#{field}").addClass 'error'
                'json'

        @comment_delete.click (evt) =>
            el = $(evt.target)
            id = el.attr('commentID')
            console.log "id is #{id}"
            $.post '/blog/comment/delete/',
                {id:id}
                (data) =>
                    if data.success
                        location.reload()
                    else
                        alert 'error on deleting comment'
                'json'




$ ->
    prettyPrint()

    page =location.pathname.split('/')[1]
    menuSetActive page

    pages_selector =
        '' : home
        'login' : login
        'blog' : blog

    pages_selector[page].init()


