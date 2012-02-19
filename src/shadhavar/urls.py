from django.conf.urls.defaults import *
import settings

# temporarily enable the admin interface
if settings.DEBUG:
    from django.contrib import admin
    admin.autodiscover()

from shadhavar.views.dashboard import DashboardView
urlpatterns = patterns('',
    url(r'^$',
        DashboardView.as_view(),
        name='dashboard')
)

urlpatterns += patterns('django.contrib.auth.views',
    (r'^accounts/login/$', 'login', {}, 'accounts_login'),
    (r'^accounts/logout/$', 'logout', {}, 'accounts_logout'),
    (r'^accounts/reset/done/$', 'password_reset_done', {}, 'accounts_reset_done'),
    (r'^accounts/reset/complete/$', 'password_reset_complete', {}, 'accounts_reset_complete'),
    (r'^accounts/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'password_reset_confirm', {}, 'accounts_reset_confirm'),
    (r'^accounts/reset/$', 'password_reset', {'post_reset_redirect': '/accounts/reset/done'}, 'accounts_reset'),
    (r'^accounts/password/$', 'password_change', {}, 'accounts_password_change'),
    (r'^accounts/password/done$', 'password_change_done', {}, 'accounts_password_change_done'),
)


import assetmanager.urls
assetpatterns = assetmanager.urls.URLs()
urlpatterns += patterns('assetmanager.views',
    (r'^assets/', include(assetpatterns.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^admin/doc/', include('django.contrib.admindocs.urls')),
        (r'^admin/', include(admin.site.urls)),
    )
