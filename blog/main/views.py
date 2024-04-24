from django.shortcuts import render
from .catalog_entry_counts import count_blog_entries_by_catalog  
from .latest_publications import latest_publications
from django.shortcuts import render, get_object_or_404
from .models import Blog, CatalogOfArticles
   
def index(request):
    return render(request, 'index.html', {
        'catalogs': count_blog_entries_by_catalog(),
        'latest_publications': latest_publications(),
        })

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk) 
    return render(request, 'blog_detail.html', {
        'blog': blog,
        'catalogs': count_blog_entries_by_catalog(),
        'latest_publications': latest_publications(),
        })
    
def catalog_name(request, pk):
    return render(request, 'category.html', {
        'catalogs': count_blog_entries_by_catalog(),
        'latest_publications': latest_publications(),
        })