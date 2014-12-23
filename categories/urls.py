from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$',            'categories.views.list',  name='category_list'),
    url(r'^add/$',        'categories.views.add',   name='category_add'),
    url(r'^show/$',       'categories.views.show_form',name='category_show'),
    url(r'^edit/(\d)+/$', 'categories.views.edit',  name='category_edit'),
    url(r'^item/(\d)+/$', 'categories.views.item',  name='category_item'),
    url(r'^delete/$',     'categories.views.delete', name='category_delete'),
)
