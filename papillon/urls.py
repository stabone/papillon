from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^poll/',  include('polls.urls')),
    url(r'^course/', include('courses.urls')),
    url(r'^user/',   include('users.urls')),
)

handler404 = 'courses.views.handler404'
