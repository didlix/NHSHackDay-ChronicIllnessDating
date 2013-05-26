from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^matches', 'nhshd.views.matches', name='matches'),
    url(r'^profile', 'nhshd.views.your_profile', name='your_profile'),
    url(r'^inbox/(?P<sender_name>[a-z0-9-_]+)', 'nhshd.views.conversation', name='conversation'),
    url(r'^inbox/?$', 'nhshd.views.inbox', name='inbox'),
    url(r'^send/(?P<username>[^/]+)$', 'nhshd.views.send_message', name='send_message'),
    url(r'^autocomplete/(?P<class_name>[a-zA-z]+)$', 'nhshd.views.autocomplete', name='autocomplete'),
    url(r'^(?P<username>[^/]+)$', 'nhshd.views.profile', name='profile'),
    url(r'^$', 'nhshd.views.home', name='home'),
)
