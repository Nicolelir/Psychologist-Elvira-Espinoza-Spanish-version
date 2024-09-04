from django.urls import path
from blog.views import my_blog

urlpatterns = [
    path('blog/', my_blog,
name='blog'),
]