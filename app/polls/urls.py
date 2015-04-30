from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<question_id>[0-9]+)/$', view.detail, name="detail"),
    url(r'^(?P<question_id>[0-9]+)/results/$', view.results, name="results"),
    url(r'^(?P<question_id)[0-9]+/vote/$', view.vote, name="vote"),
]