from django.urls import path
from .views import *


urlpatterns = [
    path('', BlogListView.as_view(), name="home"),
    path('post/<int:pk>/', BlogDetailView.as_view(), name="post-detail"),
    path('create_post/', BlogCreateView.as_view(), name="create-post"),
    path('update_post/<int:pk>/', BlogUpdateView.as_view(), name="update-post"),
    path('delete_post/<int:pk>/', BlogDeleteView.as_view(), name="delete-post"),
]