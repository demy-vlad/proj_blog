from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('category/<int:pk>/', views.catalog_name, name='catalog_name'),
]