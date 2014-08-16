from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'articles.views.index', name='article_base'),
    url(r'^add/$', 'articles.views.add', name='article_add'),
    url(r'^edit/(\d)+/$', 'articles.views.edit', name='article_edit'),
    url(r'^update/(\d)+/$', 'articles.views.update', name='article_update'),
    url(r'^delete/$', 'articles.views.delete', name='article_delete'),
)
