from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pelzoptions_project.views.home', name='home'),
    url(r'^options/', include('options.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
