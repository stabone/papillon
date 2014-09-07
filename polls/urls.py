from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^([0-9])*$', 'polls.views.index', name='base_poll'),
    url(r'^add/$', 'polls.views.add_poll', name='add_poll'),
    url(r'^add/(\d+)/(\d+)/choise/$', 'polls.views.add_choise', name='add_choise'),
    url(r'^add/question/$', 'polls.views.add_question', name='add_question'),
    url(r'^add/(\d+)/question/$', 'polls.views.add_question_for_poll', name='add_question_for_poll'),
    url(r'^edit/(\d+)/$', 'polls.views.edit_poll', name='edit_poll'),
    url(r'^edit/(\d+)/content/$', 'polls.views.edit_poll_content', name='edit_poll_content'),
    url(r'^edit/(\d+)/(\d+)/choise/$', 'polls.views.edit_choise', name='edit_choise'),
    url(r'^edit/(\d+)/question/$', 'polls.views.edit_question', name='edit_question'),
    url(r'^take/(\d+)/$', 'polls.views.take_poll', name='take_poll'),
    url(r'^statistic/$', 'polls.views.get_user_statistic', name='user_statistic'),
    url(r'^delete/poll/$', 'polls.views.delete_poll', name='delete_poll'),
    url(r'^delete/choise/$', 'polls.views.delete_choise', name='delete_choise'),
    url(r'^delete/question/$', 'polls.views.delete_question', name='delete_question'),
    url(r'^save/result/$', 'polls.views.save_poll_results', name='save_poll_results'),
)
