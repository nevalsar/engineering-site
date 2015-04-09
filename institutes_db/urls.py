from django.conf.urls import patterns, url

from institutes_db import views


urlpatterns = patterns('',
    # ex: /institutes_db/
    url(r'^$', views.index, name='index'),
    url(r'^data/$', views.table, name='table'),
    url(r'^data/(?P<profile_name>[a-z]+)/$', views.table, name='table'),
    url(r'^college/$', views.college, name='college'),
    url(r'^college/(?P<id>\d+)$', views.college, name='college'),
)
