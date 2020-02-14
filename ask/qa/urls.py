from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.new_questions, name='qa-main'),
    re_path(r'^login/$', views.test),
    re_path(r'^signup/$', views.test),
    re_path(r'^question/(?P<id>[0-9]+)/$', views.question_details, name='qa-question'),
    re_path(r'^ask/$', views.ask_question, name='qa-ask'),
    re_path(r'^popular/$', views.popular_questions, name='qa-popular'),
    re_path(r'^new/$', views.new_questions, name='qa-new'),
]
