from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name


urlpatterns = [
    path('create', BlogCreateView.as_view(), name='blog_create'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('view/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('edit/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete')

]
