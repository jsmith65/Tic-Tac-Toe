from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tic_tac_toe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('XandO.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
