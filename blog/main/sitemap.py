from django.contrib.sitemaps import Sitemap
from .models import Blog, CatalogOfArticles

class BlogSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.date_sitemap
    
class CatalogSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return CatalogOfArticles.objects.all()

    def lastmod(self, obj):
        return obj.date_sitemap