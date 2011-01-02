from django.conf.urls.defaults import *

from django.contrib.auth.views import login, logout, password_reset,\
    password_reset_done

urlpatterns = patterns('accounts',
    (r'^login/', login, {}, 'accounts_login'),
    (r'^logout/', logout, {}, 'accounts_logout'),
    (r'^reset/done/', password_reset_done, {}, 'accounts_reset_done'),
    (r'^reset/', password_reset, {'post_reset_redirect': '/accounts/reset/done'}, 'accounts_reset'),
)
