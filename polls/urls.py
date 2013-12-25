from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'polls.views.index'),
    url(r'^add/$', 'polls.views.add'),
    url(r'^edit/(\d+)/poll', 'polls.views.edit_poll'),
)
