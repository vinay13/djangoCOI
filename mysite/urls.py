
from django.conf.urls import include, url,patterns
from django.contrib import admin
from django.conf import settings
#import xadmin
#xadmin.autodiscover()


#from xadmin.plugins import xversion
#xversion.registe_models()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#    url(r'^xadmin/',include(xadmin.site.urls)),	
    url(r'^admin/', include(admin.site.urls)),
    url(r'^shot/', include('shot.urls')),
    url(r'^appy/', include('appy.urls')),	 # ADD THIS NEW TUPLE!
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
