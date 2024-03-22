from django.views.generic import CreateView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import NappyChange, User

from .forms import NappyChangeForm

class NappyChangesList(LoginRequiredMixin, ListView):
    """View list of recent nappy changes"""
    template_name = 'nappy_changes/nappy_changes_list.html'
    model = NappyChange
    context_object_name = 'nappy_changes_list'
    

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