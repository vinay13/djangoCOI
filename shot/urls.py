from django.conf.urls import patterns, url
from shot import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
	url(r'^category/(?P<slug>[\w\-]+)/$', views.category, name='category'),)
