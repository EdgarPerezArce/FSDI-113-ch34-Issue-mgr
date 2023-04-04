from django.urls import path
from issues import views


urlpatters = [
    path("", views.IssueListView.as_view(), name="list"),
    path("<int:pk>/", views.IssueListView.as_view(), name="list"),
    path("<int:pk>/edit/", views.IssueListView.as_view(), name="list"),
    path("<int:pk>/delete/", views.IssueListView.as_view(), name="list"),
    path("new/", views.IssueListView.as_view(), name="list"),
]