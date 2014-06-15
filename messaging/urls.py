from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$',       'messaging.views.inbox', name='messaging_inbox'),
    url(r'^add/$',   'messaging.views.add_message', name='messaging_add'),
    url(r'^read/(\d+)/$', 'messaging.views.read_message', name='messaging_read'),
    url(r'^trash/$', 'messaging.views.trash_message', name='messaging_trash'),
    url(r'^to/trash/$', 'messaging.views.to_trash_message', name='messaging_to_trash'),
    url(r'^delete/(\d+)/$', 'messaging.views.delete_message', name='messaging_delete'),
)
