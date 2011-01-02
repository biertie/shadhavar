from django.conf.urls.defaults import *

from django.contrib.auth.views import login

urlpatterns = patterns('accounts',
    (r'^login/', login, {'template_name': 'accounts/login.html', 'redirect_field_name': 'next'}),
)
