from django.conf.urls.defaults import *
import settings

# temporarily enable the admin interface
if settings.DEBUG:
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

import django.views.generic
import assetmanager.models
urlpatterns += patterns('django.views.generic',
    (r'^assets/datacentre/$', 'list_detail.object_list', {'queryset' : assetmanager.models.Datacentre.objects.all()}, 'datacentre_index'),
    (r'^assets/datacentre/(?P<object_id>[0-9]+)/$', 'list_detail.object_detail', {'queryset': assetmanager.models.Datacentre.objects.all()}, 'datacentre_detail'),
    (r'^assets/datacentre/add/$', 'create_update.create_object', {'model': assetmanager.models.Datacentre, 'post_save_redirect': '/assets/datacentre/'}, 'datacentre_add'),
    (r'^assets/datacentre/edit/(?P<object_id>[0-9]+)/$', 'create_update.update_object', {'model': assetmanager.models.Datacentre, 'post_save_redirect': '/assets/datacentre/'}, 'datacentre_update'),
    (r'^assets/datacentre/delete/(?P<object_id>[0-9]+)/$', 'create_update.delete_object', {'model': assetmanager.models.Datacentre, 'post_delete_redirect': '/assets/datacentre/'}, 'datacentre_delete'),

    (r'^assets/serverroom/$', 'list_detail.object_list', {'queryset': assetmanager.models.Serverroom.objects.all()}, 'serverroom_index'),
    (r'^assets/serverroom/(?P<object_id>[0-9]+)/$', 'list_detail.object_detail', {'queryset': assetmanager.models.Serverroom.objects.all()}, 'serverroom_detail'),
    (r'^assets/serverroom/add/$', 'create_update.create_object', {'model': assetmanager.models.Serverroom, 'post_save_redirect': '/assets/serverroom/'}, 'serverroom_add'),
    (r'^assets/serverroom/edit/(?P<object_id>[0-9]+)/$', 'create_update.update_object', {'model': assetmanager.models.Serverroom, 'post_save_redirect': '/assets/serverroom/'}, 'serverroom_update'),
    (r'^assets/serverroom/delete/(?P<object_id>[0-9]+)/$', 'create_update.delete_object', {'model': assetmanager.models.Serverroom, 'post_delete_redirect': '/assets/serverroom/'}, 'serverroom_delete'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^admin/doc/', include('django.contrib.admindocs.urls')),
        (r'^admin/', include(admin.site.urls)),
    )
