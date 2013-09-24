from django.conf.urls import patterns, include, url
from mucu.views import *

from django.contrib import admin



admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',            main),
    url(r'^aboutUs/',     aboutUs),
    url(r'^admin/',       include(admin.site.urls)),
    url(r'^departments/', departments),
    url(r'^fellowship/',    fellowships),
    url(r'^gallery/',     gallery),
    url(r'^summons/',     summons),
    url(r'^contacts/',    contacts),
    url(r'^sendMail/',    send_my_mail),
    url(r'^news_letter/', news_letter)
)
