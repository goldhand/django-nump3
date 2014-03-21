from django.conf.urls import patterns, url

from .views import Mp3List, Mp3Detail



urlpatterns = patterns('',
	url(r'^$', Mp3List.as_view(), name='list'),
	# allows slugs to contain [_, -]
	#url(r'^(?P<slug>[-_\w]+)/$', Mp3Detail.as_view(), name='detail'),
	# allows anything to be a slug
	url(r'^(?P<page_slug>.*)/(?P<slug>.*)/$', Mp3Detail.as_view(), name='detail'),
	
)