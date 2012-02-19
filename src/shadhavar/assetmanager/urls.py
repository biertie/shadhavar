from django.conf.urls.defaults import patterns, url
import assetmanager.models as models
import assetmanager.views as views
import views.base as generic
from django.utils._os import safe_join
from django.conf import settings

class URLs:
    def get_urls(self):
        urlpatterns = []
        CRUD = {'List': '',
                'Detail': '(?P<pk>[0-9]+)/',
                'Create': 'add/',
                'Update': 'edit/(?P<pk>[0-9]+)/',
                'Delete': 'delete/(?P<pk>[0-9]+)/',}
        for name in dir(models):
            if name[:2] == '__' or name == 'models':
                continue
            for key,value in CRUD.iteritems():
                action = '{0}_{1}'.format(name.lower(), key.lower())

                # try to fetch a custom ClassActionView
                viewname = '{0}{1}View'.format(name, key)
                view = getattr(views, viewname, None)

                # but fall back on the generic *Views from django
                if not view:
                    viewname = 'Base{0}View'.format(key)
                    view = getattr(generic, viewname)
                    view.model = getattr(models, name)

                # see if a custom template exists
                base = 'assetmanager/{0}.html'
                gener = base.format('base_{0}')
                template = gener.format(key.lower())
                for template_dir in settings.TEMPLATE_DIRS:
                    try:
                        path = safe_join(template_dir,
                                base.format(action))
                        f = open(path)
                        if f:
                            template = base.format(action)
                        f.close()
                    except:
                        continue
                view.template_name = template

                urlpatterns += patterns('',
                    url(r'^{0}/{1}$'.format(name.lower(), value),
                        view.as_view(model=view.model, template_name=template),
                        name=action)
                    )
        return urlpatterns

    urls = property(get_urls)
