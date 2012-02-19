from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class BaseCreateView(CreateView):
    def get_context_data(self, **kwargs):
        context = super(BaseCreateView, self).get_context_data(**kwargs)
        context["classname"] = self.model.__name__
        return context

class BaseDeleteView(DeleteView):
    def get_context_data(self, **kwargs):
        context = super(BaseDeleteView, self).get_context_data(**kwargs)
        context["classname"] = self.model.__name__
        blacklist = ['_state']
        blacklist.extend(dir(self.model))
        context["fields"] = []
        for f in [x for x in dir(context["object"]) if x not in blacklist]:
            context["fields"].append((f, getattr(context["object"], f)))
        return context

class BaseListView(ListView):
    def get_context_data(self, **kwargs):
        context = super(BaseListView, self).get_context_data(**kwargs)
        context["classname"] = self.model.__name__
        blacklist = ['_state']
        blacklist.extend(dir(self.model))
        context["fields"] = [x for x in dir(context["object_list"][0]) if x not in blacklist]
        # just because the templating system won't let us access stuff by var
        # without implementing a custom filter
        context["objects"] = []
        for obj in context["object_list"]:
            tmp = []
            for f in context["fields"]:
                tmp.append(getattr(obj, f))
            context["objects"].append(tmp)
        return context

class BaseDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super(BaseDetailView, self).get_context_data(**kwargs)
        context["classname"] = self.model.__name__
        blacklist = ['_state']
        blacklist.extend(dir(self.model))
        context["fields"] = [x for x in dir(context["object"]) if x not in blacklist]
        return context

class BaseUpdateView(UpdateView):
    def get_context_data(self, **kwargs):
        context = super(BaseUpdateView, self).get_context_data(**kwargs)
        context["classname"] = self.model.__name__
        blacklist = ['_state']
        blacklist.extend(dir(self.model))
        context["fields"] = [x for x in dir(context["object"]) if x not in blacklist]
        return context
