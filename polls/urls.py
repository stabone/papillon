from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^([0-9]*)$', 'polls.views.index'),
    url(r'^add/poll/$', 'polls.views.add_poll'),
    url(r'^add/(\d+)/(\d+)/choise/$', 'polls.views.add_choise'),
    url(r'^add/(\d+)/question/$', 'polls.views.add_question'),
    url(r'^edit/(\d+)/poll/$', 'polls.views.edit_poll'),
    url(r'^edit/(\d+)/choise/$', 'polls.views.edit_choise'),
    url(r'^edit/(\d+)/question/$', 'polls.views.edit_question'),
    url(r'^take/(\d+)/poll/$', 'polls.views.take_poll'),
    url(r'^take/(\d+)/question/$', 'polls.views.take_question'),
    url(r'^delete/(\d+)/poll/$', 'polls.views.delete_poll'),
    url(r'^delete/(\d+)/choise/$', 'polls.views.delete_choise'),
    url(r'^delete/(\d+)/question/$', 'polls.views.delete_question'),
)
