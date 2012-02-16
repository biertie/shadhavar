#from shadhavar import settings
from django.views.generic import TemplateView

class BaseView(TemplateView):
    def __init__(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(PublisherDetailView, self).get_context_data(**kwargs)
        context['STATIC_URL'] = settings.STATIC_URL
        return context
