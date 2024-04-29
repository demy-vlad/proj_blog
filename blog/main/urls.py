from . import views
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemap import BlogSitemap, CatalogSitemap

sitemaps = {
    'blog': BlogSitemap,
    'category': CatalogSitemap,
    # Додайте інші карти сайту, якщо потрібно
}

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<str:slug>/', views.blog_detail, name='blog_detail'),
    path('category/<str:slug>/', views.catalog_name, name='catalog_name'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]