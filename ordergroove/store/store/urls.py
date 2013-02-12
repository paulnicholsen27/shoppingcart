from django.conf.urls import patterns, include, url
#from inventory.views import homepage, products, shoppingcart, checkout
from store import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<store_subdomain>\w+)/$', 'inventory.views.homepage'),
    url(r'^(?P<store_subdomain>\w+)/products/$', 'inventory.views.products'),
    url(r'^(?P<store_subdomain>\w+)/shoppingcart/$', 'inventory.views.shoppingcart'),
    url(r'^(?P<store_subdomain>\w+)/checkout/$', 'inventory.views.checkout'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    	{'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
)
