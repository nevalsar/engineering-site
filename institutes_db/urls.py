from django.conf.urls import patterns, url

from institutes_db import views


urlpatterns = patterns('',
    # ex: /institutes_db/
    url(r'^$', views.index, name='index'),
    url(r'^data/(?P<profile_name>[a-z]+)/$', views.table, name='table'),
)
