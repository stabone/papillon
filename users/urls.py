from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'users.views.index', name='user_base'),
    url(r'^registration/$', 'users.views.registration', name='user_registration'),
    url(r'^profile/$', 'users.views.user_profile', name='user_profile'),
    url(r'^email/send/$', 'users.views.send_notification', name='send_notification'),
    url(r'^find/$', 'users.views.find_user', name='user_find'),
    url(r'^edit/$', 'users.views.user_edit', name='user_edit'),
    url(r'^delete/$', 'users.views.user_delete', name='user_delete'),
    url(r'^add/group/$', 'users.views.create_group', name='group_add'),
)
