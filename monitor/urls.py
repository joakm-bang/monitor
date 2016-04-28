from django.conf.urls import url

from . import views

app_name = 'monitor'  # name spacing the URL names

# regular expression for the url, sends it to views.index, name is for global cahnges to the pattern (?)
urlpatterns = [
    # ex: /monitor/
    url(r'^activity/$', views.activity, name='activity'),
    ## ex: /monitor/5/
    #url(r'^(?P<computer_name>[a-z]+)/$', views.detail, name='detail'),
    ## ex: /monitor/5/activity/
    #url(r'^(?P<computer_name>[a-z]+)/activity/$', views.latest, name='latest'),    
]