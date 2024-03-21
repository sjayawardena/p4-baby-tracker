from django.views.generic import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import NappyChange

from .forms import NappyChangeForm


class AddNappyChange(LoginRequiredMixin, CreateView):
    """
    Add nappy change view
    """
    template_name = 'nappy_changes/add_nappy_change.html'
    model = NappyChange
    form_class = NappyChangeForm
    success_url = '/nappy_changes'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddNappyChange, self).form_valid(form)