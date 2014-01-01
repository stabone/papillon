from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'polls.views.index'),
    url(r'^add/poll/$', 'polls.views.add_poll'),
    url(r'^add/choise/$', 'polls.views.add_choise'),
    url(r'^edit/(\d+)/poll/$', 'polls.views.edit_poll'),
    url(r'^edit/(\d+)/choise/$', 'polls.views.edit_choise'),
    url(r'^take/(\d+)/poll/$', 'polls.views.take_poll'),
)
