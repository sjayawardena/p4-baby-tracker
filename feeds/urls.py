from django.urls import path
from .views import AddFeed, FeedsList, DeleteFeed, EditFeed, FeedDetail


urlpatterns = [
    path('', AddFeed.as_view(), name = 'add_feed'),
    path('feeds_list/', FeedsList.as_view(), name = 'feeds_list'),
    path("<slug:pk>/", FeedDetail.as_view(), name="feed_detail"),
    path('delete/<slug:pk>/', DeleteFeed.as_view(), name='delete_feed'),
    path('edit/<slug:pk>/', EditFeed.as_view(), name='edit_feed'),
]