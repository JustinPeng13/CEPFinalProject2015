from django.conf.urls import patterns, include, url
from django.contrib import admin
from totalfeed import views

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.MainView.as_view()),
	url(r'^ajax/', include('update.urls')),
	url(r'account/', include('accounts.urls')),
	url(r'^(?P<site>.*)/$', views.SiteView.as_view()),
)