from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'comments.views.index', name='comments'),
    url(r'^video/get/comment/$', 'comments.views.get_video_comments', name='get_video_comments'),
    url(r'^video/show/comment/$', 'comments.views.show_all_comments', name='show_all_comments'),
    url(r'^video/add/poll/$', 'comments.views.get_poll_comments', name='get_poll_comments'),
)
