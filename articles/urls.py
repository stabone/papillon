from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^([0-9])*$', 'articles.views.index', name='article_base'),
    url(r'^add/$', 'articles.views.add', name='article_add'),
    url(r'^edit/(\d)+/$', 'articles.views.edit', name='article_edit'),
    url(r'^update/(\d)+/$', 'articles.views.update', name='article_update'),
    url(r'^item/(\d)+/$', 'articles.views.item', name='article_item'),
    url(r'^delete/$', 'articles.views.delete', name='article_delete'),

    url(r'^a/$', 'articles.views.list_review', name='review_base'),
    url(r'^a/add/$', 'articles.views.add_review', name='review_add'),
    url(r'^a/edit/$', 'articles.views.edit_review', name='review_edit'),
    url(r'^a/update/$', 'articles.views.update_review', name='review_update'),
    url(r'^a/delete/*$', 'articles.views.delete_review', name='review_delete'),
)
