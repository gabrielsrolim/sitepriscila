from django.conf.urls.defaults import patterns, include, url
from cibereducacao.views import *
from cibereducacao.books import views
from cibereducacao.contact.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #('^$', my_homepage_view),
    (r'^hello/$',hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^display/$',display_meta),
    (r'^contact/$', contact),
    (r'^search/$', views.search),
    # Examples:
    # url(r'^$', 'cibereducacao.views.home', name='home'),
    # url(r'^cibereducacao/', include('cibereducacao.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
