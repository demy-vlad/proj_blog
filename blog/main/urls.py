from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<str:slug>/', views.blog_detail, name='blog_detail'),
    path('category/<str:slug>/', views.catalog_name, name='catalog_name'),
]