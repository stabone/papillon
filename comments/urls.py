from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'comments.views.index', name='comments'),
    url(r'^video/add/comment/$', 'comments.views.video_comments', name='video_comments'),
    url(r'^video/show/comment/$', 'comments.views.show_comments', name='show_comments'),
    url(r'^video/add/poll/$', 'comments.views.poll_comments', name='poll_comments'),
)
