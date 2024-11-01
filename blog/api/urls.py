from django.urls import path
from .views import BlogDetails

urlpatterns = [
    path('blogs/', BlogDetails.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogDetails.as_view(), name='blog-detail')
]
