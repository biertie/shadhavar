from django.conf.urls.defaults import *

from django.contrib.auth.views import login, logout

urlpatterns = patterns('accounts',
    (r'^login/', login, {}),
    (r'^logout/', logout, {}),
)
