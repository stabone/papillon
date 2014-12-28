from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^list/$',      'polls.views.poll_list',   name='poll_list'),
    url(r'^form/$',      'polls.views.poll_form',   name='poll_form'),
    url(r'^create/$',    'polls.views.poll_create', name='poll_create'),
    url(r'^edit/(\d+)/$','polls.views.poll_edit',   name='poll_edit'),
    url(r'^item/(\d+)/$','polls.views.poll_item',   name='poll_item'),
    url(r'^update/$',    'polls.views.poll_update', name='poll_update'),
    url(r'^delete/$',    'polls.views.poll_delete', name='poll_delete'),


    url(r'^q/list/$',      'polls.views.question_list',   name='question_list'),
    url(r'^q/form/(\d+)/$','polls.views.question_form',   name='question_form'),
    url(r'^q/create/$',    'polls.views.question_create', name='question_create'),
    url(r'^q/edit/(\d+)/$','polls.views.question_edit',   name='question_edit'),
    url(r'^q/update/$',    'polls.views.question_update', name='question_update'),
    url(r'^q/delete/$',    'polls.views.question_delete', name='question_delete'),


    url(r'^a/list/$',      'polls.views.answer_list',   name='answer_list'),
    url(r'^a/form/(\d+)/$','polls.views.answer_form',   name='answer_form'),
    url(r'^a/create/$',    'polls.views.answer_create', name='answer_create'),
    url(r'^a/edit/(\d+)/$','polls.views.answer_edit',   name='answer_edit'),
    url(r'^a/update/$',    'polls.views.answer_update', name='answer_update'),
    url(r'^a/delete/$',    'polls.views.answer_delete', name='answer_delete'),

)
