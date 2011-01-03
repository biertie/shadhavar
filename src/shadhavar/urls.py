from django.conf.urls.defaults import *

# temporarily enable the admin interface
from django.contrib import admin
admin.autodiscover()

import django.contrib.auth.views
urlpatterns = patterns('',
    (r'^accounts/login/$', django.contrib.auth.views.login, {}, 'accounts_login'),
    (r'^accounts/logout/$', django.contrib.auth.views.logout, {}, 'accounts_logout'),
    (r'^accounts/reset/done/$', django.contrib.auth.views.password_reset_done, {}, 'accounts_reset_done'),
    (r'^accounts/reset/complete/$', django.contrib.auth.views.password_reset_complete, {}, 'accounts_reset_complete'),
    (r'^accounts/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', django.contrib.auth.views.password_reset_confirm, {}, 'accounts_reset_confirm'),
    (r'^accounts/reset/$', django.contrib.auth.views.password_reset, {'post_reset_redirect': '/accounts/reset/done'}, 'accounts_reset'),
    (r'^accounts/password/$', django.contrib.auth.views.password_change, {}, 'accounts_password_change'),
    (r'^accounts/password/done$', django.contrib.auth.views.password_change_done, {}, 'accounts_password_change_done'),
)

urlpatterns += patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
