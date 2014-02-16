from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'users.views.index'),
    url(r'^create/$', 'users.views.create', name='create_user'),
    url(r'^register/$', 'users.views.register', name='register_user'),
    url(r'^email/send/$', 'users.views.send_notification', name='send_notification'),
)
