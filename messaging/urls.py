from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^([0-9])*$', 'messaging.views.inbox', name='messaging_inbox'),
    url(r'^add/$', 'messaging.views.add_message', name='messaging_add'),
    url(r'^read/(\d+)/$', 'messaging.views.read_message', name='messaging_read'),
    url(r'^respond/(\d+)/$', 'messaging.views.respond_message', name='messaging_respond'),
    url(r'^restore/$', 'messaging.views.restore_message', name='messaging_restore'),
    url(r'^trash/([0-9])*$', 'messaging.views.trash_message', name='messaging_trash'),
    url(r'^to/trash/$', 'messaging.views.to_trash_message', name='messaging_to_trash'),
    url(r'^contact/delete/$', 'messaging.views.delete_contact', name='contact_list'),
    url(r'^delete/$', 'messaging.views.delete_message', name='messaging_delete'),
    url(r'^delete/list/$', 'messaging.views.delete_message_list', name='msg_list_delete'),
)
