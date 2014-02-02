from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'users.views.index'),
    url(r'^create/$', 'users.views.create'),
    url(r'^register/$', 'users.views.register'),
    url(r'^email/send/$', 'users.views.send_notification'),
)
