from django.conf.urls import patterns, include, url
from mucu.views import *
from django.contrib import admin



admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',           main),
    url(r'^aboutUs/',    aboutUs),
    url(r'^admin/',      include(admin.site.urls)),
    url(r'^leadership/',  leadership),
    url(r'^partners/',    partners),
    url(r'^gallery/',     gallery),
    url(r'^summons/',     summons),
    url(r'^contacts/',    contacts),
)
