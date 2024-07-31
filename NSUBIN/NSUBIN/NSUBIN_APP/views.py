from time import timezone
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .models import NsuBinModel
from .forms import NsuBinForm

# Create your views here.
class NsuBinView(CreateView):
    model = NsuBinModel
    form_class = NsuBinForm
    template_name = 'nsubin.html'
    success_url = reverse_lazy('nsubin')
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        self.object = form.save()
        # NsuBinModel.objects.filter(created_at__lte=timezone.now() - timezone.timedelta(minutes=10)).delete()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = NsuBinModel.objects.all()
        return context
    
class NsuBinEditView(UpdateView):
    model = NsuBinModel
    form_class = NsuBinForm
    template_name = 'nsubin.html'
    success_url = reverse_lazy('nsubin')

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    
    

