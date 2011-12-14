from django.conf.urls.defaults import patterns, include, url
from django.views.generic import list_detail
from stanley_darpa.models import Event

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Project.views.home', name='home'),
    # url(r'^Project/', include('Project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'stanley_darpa.views.index'),
    url(r'^rules$', 'stanley_darpa.views.rules'),
    url(r'^submit$', 'stanley_darpa.views.submit'),
    url(r'^countdown$', 'stanley_darpa.views.countdown'),
    url(r'^cities$', 'stanley_darpa.views.cities'),
#    url(r'^team', 'stanley_darpa.views.teamDetail'),

    url(r'^getEvents$', 'stanley_darpa.views.getEvents'),
    url(r'^addEvent$', 'stanley_darpa.views.addRandomEvent'),

#    url(r'^upload', 'stanley_darpa.views.upload_file'),
)

