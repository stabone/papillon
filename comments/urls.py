from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'comments.views.index', name='comments'),
    url(r'^video/$', 'comments.views.video_comments', name='video_comments'),
)
