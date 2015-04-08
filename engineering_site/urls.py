from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'engineering_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^institutes_db/', include('institutes_db.urls', namespace="institutes_db")),
    url(r'^admin/', include(admin.site.urls)),
)
