
from django.conf.urls import patterns, url
from appy import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
	url(r'^type/(?P<slug>[\w\-]+)/$', views.show, name='show'),)
