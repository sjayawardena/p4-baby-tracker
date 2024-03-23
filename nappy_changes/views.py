from django.views.generic import CreateView, DetailView, DeleteView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import NappyChange, User

from .forms import NappyChangeForm

class NappyChangesList(LoginRequiredMixin, ListView):
    """View list of recent nappy changes"""
    template_name = 'nappy_changes/nappy_changes_list.html'
    model = NappyChange
    context_object_name = 'nappy_changes_list'
    
    def get_queryset(self):
        return self.request.user.nappy_changes_list.all()
    


class AddNappyChange(LoginRequiredMixin, CreateView):
    """
    Add nappy change view
    """
    template_name = 'nappy_changes/add_nappy_change.html'
    model = NappyChange
    form_class = NappyChangeForm
    success_url = 'nappy_changes_list/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddNappyChange, self).form_valid(form)
    

class DeleteNappyChange(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a nappy change entry - with check that logged in user is deleting only their own entries"""
    model = NappyChange
    template_name = 'nappy_changes/nappy_change_confirm_delete.html'
    success_url = 'nappy_changes/templates/nappy_changes/nappy_changes_list.html'
    
    def test_func(self):
        return self.request.user == self.get_object().user
    