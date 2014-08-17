from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',       include('helper.urls')),
    url(r'^admin/',  include(admin.site.urls)),
    url(r'^poll/',   include('polls.urls')),
    url(r'^course/', include('courses.urls')),
    url(r'^user/',   include('users.urls')),
    url(r'^comment/',include('comments.urls')),
    url(r'^message/', include('messaging.urls')),
    url(r'^markdown/', include( 'django_markdown.urls')),
    url(r'^article/', include('articles.urls')),
    url(r'^login/',  'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}, name='user_login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='user_logout'),
)

handler400 = 'helper.views.handler400'
handler403 = 'helper.views.handler403'
handler404 = 'helper.views.handler404'
handler500 = 'helper.views.handler500'

