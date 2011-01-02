from django.conf.urls.defaults import *

from django.contrib.auth.views import login, logout

urlpatterns = patterns('accounts',
    (r'^login/', login, {'template_name': 'accounts/login.html'}),
    (r'^logout/', logout, {'template_name': 'accounts/logout.html', 'next_page': '/'}),
)
