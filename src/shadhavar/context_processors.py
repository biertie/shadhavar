import assetmanager.models as assetmodels
from django.core.urlresolvers import reverse

def menu(req):
    # need to figure out a way to prevent django from silly sorting
    ret = {}
    ret['menu'] = {}
    for action in ['List', 'Create']:
        ret['menu'][action] = {}
        for name in dir(assetmodels):
            if name[:2] == '__' or name == 'models':
                continue
            urlname = '{0}_{1}'.format(name.lower(), action.lower())
            ret['menu'][action][name] = reverse(urlname)
    return ret
