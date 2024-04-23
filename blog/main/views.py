from django.shortcuts import render
from .models import CatalogOfArticles, Blog

def get_catalog_names_by_title():
    catalogs = CatalogOfArticles.objects.all()

def index(request):
    catalogs = CatalogOfArticles.objects.all()
    catalog_count = catalogs.count()
    return render(request, 'index.html', {'catalogs': catalogs, 'catalog_count': catalog_count})