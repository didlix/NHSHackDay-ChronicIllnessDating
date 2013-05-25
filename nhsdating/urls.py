from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search', include('haystack.urls')),
    url(r'^(?P<username>[^/]+)$', 'nhshd.views.profile', name='profile'),
    url(r'^$', 'nhshd.views.home', name='home'),
)
