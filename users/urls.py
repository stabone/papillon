from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'users.views.index', name='user_base'),
    url(r'^registration/$', 'users.views.registration', name='user_registration'),
    url(r'^profile/$', 'users.views.user_profile', name='user_profile'),
    url(r'^find/$', 'users.views.find_user', name='user_find'),
    url(r'^edit/$', 'users.views.user_edit', name='user_edit'),
    url(r'^delete/$', 'users.views.user_delete', name='user_delete'),
    url(r'^group/$', 'users.views.list_groups', name='group_list'),
    url(r'^add/group/$', 'users.views.add_group', name='group_add'),
    url(r'^edit/(\d+)/group/$', 'users.views.edit_group', name='group_edit'),
    url(r'^update/group/$', 'users.views.update_group', name='group_update'),
    url(r'^delete/group/$', 'users.views.delete_group', name='group_delete'),
    url(r'^create/group/$', 'users.views.create_group', name='group_create'),
    url(r'^add/perms/$', 'users.views.add_group_perms', name='group_perms_add'),

    url(r'^create/admin/$', 'users.views.create_admin', name='create_admin'),
)
