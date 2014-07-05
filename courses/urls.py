from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$',                  'courses.views.index', name='base_course'),
    url(r'^add/course/$',       'courses.views.add_categorie', name='add_course'),
    url(r'^add/(\d+)/tut/$',    'courses.views.add_tut', name='add_tut'),
    url(r'^add/(\d+)/material/$', 'courses.views.add_material', name='add_material'),
    url(r'^edit/(\d+)/course/$','courses.views.edit_categorie', name='edit_categorie'),
    url(r'^edit/(\d+)/tut/$',   'courses.views.edit_tut', name='edit_tut'),
    url(r'^show/(\d+)/course/$','courses.views.show_categorie', name='show_categorie'),
    url(r'^show/(\d+)/tut/$',   'courses.views.show_tut', name='show_tut'),
    url(r'^tut/rate/$',   'courses.views.rate_tut', name='rate_tut'),
    url(r'^show/(\d+)/material/$', 'courses.views.show_material', name='show_material'),
    url(r'^delete/course/$', 'courses.views.delete_categorie', name='delete_categorie'),
    url(r'^delete/tut/$', 'courses.views.delete_tut', name='delete_tut'),
    url(r'^delete/material/$', 'courses.views.delete_material', name='delete_material'),
)
