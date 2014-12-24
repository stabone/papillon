from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$',            'categories.views.list',  name='category_list'),
    url(r'^create/$',     'categories.views.create',name='category_create'),
    url(r'^form/$',       'categories.views.form',  name='category_form'),
    url(r'^edit/(\d)+/$', 'categories.views.edit',  name='category_edit'),
    url(r'^update/$',     'categories.views.update',name='category_update'),
    url(r'^item/(\d)+/$', 'categories.views.item',  name='category_item'),
    url(r'^delete/$',     'categories.views.delete', name='category_delete'),
)
