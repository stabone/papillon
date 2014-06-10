from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'users.views.index'),
    # url(r'^create/$', 'users.views.create', name='user_create'),
    url(r'^registration/$', 'users.views.registration', name='user_registration'),
    url(r'^profile/$', 'users.views.user_profile', name='user_profile'),
    url(r'^email/send/$', 'users.views.send_notification', name='send_notification'),
)
