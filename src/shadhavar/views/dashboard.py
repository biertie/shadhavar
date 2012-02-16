from base import BaseView

class DashboardView(BaseView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        return context
