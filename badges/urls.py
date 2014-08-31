from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'badges.views.get_badges', name='badge_base'),
    url(r'^add/$', 'badges.views.add_badge', name='badge_add'),
    url(r'^edit/(\d+)/$', 'badges.views.edit_badge', name='badge_edit'),
    url(r'^delete/$', 'badges.views.delete_badge', name='badge_delete'),
    url(r'^add/type$', 'badges.views.add_badge_type', name='badge_type'),
    url(r'^edit/type/(\d+)$', 'badges.views.edit_badge_type', name='badge_type_edit'),
    url(r'^delete/type/$', 'badges.views.delete_badge_type', name='badge_type_delete'),
)
