from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'comments.views.index'),
    url(r'^video/$', 'comments.views.video_comments'),
)
