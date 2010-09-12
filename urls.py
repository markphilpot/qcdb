from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qcdb.web.views',
    # Example:
    # (r'^qcdb/', include('qcdb.foo.urls')),

    (r'^$', 'index'),
    #(r'^comics/$', 'comics'),
    (r'^comics/(?P<comic_id>\d+)/$', 'comic'),
    #(r'^characters/$', 'characters'),
    #(r'^characters/(?P<character_id>\d+)/$', 'character'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls))
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )


