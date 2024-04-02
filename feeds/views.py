from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView,
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy

from .models import Feed, User

from .forms import FeedForm


class FeedsList(LoginRequiredMixin, ListView):
    """View list of recent feeds"""

    template_name = "feeds/feeds_list.html"
    model = Feed
    context_object_name = "feeds_list"

    def get_queryset(self):
        return self.request.user.feeds_list.all()


class FeedDetail(LoginRequiredMixin, DetailView):
    """View a single feed entry"""

    template_name = "feeds/feed_detail.html"
    model = Feed
    context_object_name = "feed"


class AddFeed(LoginRequiredMixin, CreateView):
    """
    Add feed view
    """

    template_name = "feeds/add_feed.html"
    model = Feed
    form_class = FeedForm
    success_url = reverse_lazy("feeds_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddFeed, self).form_valid(form)


class EditFeed(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a feedentry - with check that logged in user is editing only their own entries"""

    template_name = "feeds/edit_feed.html"
    model = Feed
    form_class = FeedForm
    success_url = reverse_lazy("feeds_list")

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteFeed(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a nappy change entry - with check that logged in user is deleting only their own entries"""

    model = Feed
    template_name = "feeds/feed_confirm_delete.html"
    success_url = reverse_lazy("feeds_list")

    def test_func(self):
        return self.request.user == self.get_object().user
