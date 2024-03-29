from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
    ListView,
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy

from .models import NappyChange, User

from .forms import NappyChangeForm


class NappyChangesList(LoginRequiredMixin, ListView):
    """View list of recent nappy changes"""

    template_name = "nappy_changes/nappy_changes_list.html"
    model = NappyChange
    context_object_name = "nappy_changes_list"

    def get_queryset(self):
        return self.request.user.nappy_changes_list.all()


class NappyChangeDetail(LoginRequiredMixin, DetailView):
    """View a single nappy change entry"""

    template_name = "nappy_changes/nappy_change_detail.html"
    model = NappyChange
    context_object_name = "nappy_change"


class AddNappyChange(LoginRequiredMixin, CreateView):
    """
    Add nappy change view
    """

    template_name = "nappy_changes/add_nappy_change.html"
    model = NappyChange
    form_class = NappyChangeForm
    success_url = reverse_lazy("nappy_changes_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddNappyChange, self).form_valid(form)


class EditNappyChange(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a nappy change entry - with check that logged in user is editing only their own entries"""

    template_name = "nappy_changes/edit_nappy_change.html"
    model = NappyChange
    form_class = NappyChangeForm
    success_url = reverse_lazy("nappy_changes_list")

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteNappyChange(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a nappy change entry - with check that logged in user is deleting only their own entries"""

    model = NappyChange
    template_name = "nappy_changes/nappy_change_confirm_delete.html"
    success_url = reverse_lazy("nappy_changes_list")

    def test_func(self):
        return self.request.user == self.get_object().user
