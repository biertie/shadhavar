from django.conf.urls.defaults import *

from django.contrib.auth.views import login, logout, password_reset,\
    password_reset_done, password_reset_confirm, password_reset_complete,\
    password_change, password_change_done

urlpatterns = patterns('accounts',
    (r'^login/$', login, {}, 'accounts_login'),
    (r'^logout/$', logout, {}, 'accounts_logout'),
    (r'^reset/done/$', password_reset_done, {}, 'accounts_reset_done'),
    (r'^reset/complete/$', password_reset_complete, {}, 'accounts_reset_complete'),
    (r'^reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {}, 'accounts_reset_confirm'),
    (r'^reset/$', password_reset, {'post_reset_redirect': '/accounts/reset/done'}, 'accounts_reset'),
    (r'^password/$', password_change, {}, 'accounts_password_change'),
    (r'^password/done$', password_change_done, {}, 'accounts_password_change_done'),
)
