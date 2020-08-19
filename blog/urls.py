from django.urls import path
from .views import BlogListView, blog_detail

app_name = 'blog'

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog-home'),
    path('blog/<id>/', blog_detail, name='blog-detail')
]