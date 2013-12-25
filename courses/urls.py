from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$',                  'courses.views.index'),
    url(r'^add/course/$',       'courses.views.add_categorie'),
    url(r'^add/tut/$',          'courses.views.add_tut'),
    url(r'^edit/(\d+)/course/$','courses.views.edit_categorie'),
    url(r'^edit/(\d+)/tut/$',   'courses.views.edit_tut'),
    url(r'^show/(\d+)/course/$','courses.views.show_categorie'),
    url(r'^show/(\d+)/tut/$',   'courses.views.show_tut'),
    url(r'^delete/(\d+)/course/$', 'courses.views.delete_categorie'),
    url(r'^delete/(\d+)/tut/$', 'courses.views.delete_tut'),
)
