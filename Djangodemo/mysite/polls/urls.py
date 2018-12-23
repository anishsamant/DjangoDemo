from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    #$ means we dont want to add anything extra to the current url.
    #second argument tells what we want to display
    #third argument is the name of our function

    url(r'^$', views.index, name="index"), #url will look like 127.0.0.1/polls
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"), #url will look like 127.0.0.1/polls/1
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name="results"), #url will look like 127.0.0.1/polls/1/results
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"), #url will look like 127.0.0.1/polls/1/vote
]