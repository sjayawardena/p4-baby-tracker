from django.urls import path
from .views import (
    AddNappyChange,
    NappyChangesList,
    DeleteNappyChange,
    EditNappyChange,
    NappyChangeDetail,
)

urlpatterns = [
    path("", AddNappyChange.as_view(), name="add_nappy_change"),
    path("nappy_changes_list/", NappyChangesList.as_view(),
         name="nappy_changes_list"),
    path("<slug:pk>/", NappyChangeDetail.as_view(),
         name="nappy_change_detail"),
    path("delete/<slug:pk>/", DeleteNappyChange.as_view(),
         name="delete_nappy_change"),
    path("edit/<slug:pk>/", EditNappyChange.as_view(),
         name="edit_nappy_change"),
]
