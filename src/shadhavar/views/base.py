from shadhavar import settings
from django.views.generic import TemplateView

class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['STATIC_URL'] = settings.STATIC_URL
        return context
