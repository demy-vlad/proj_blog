from django.shortcuts import render
from .catalog_entry_counts import count_blog_entries_by_catalog  
from .latest_publications import latest_publications
from django.shortcuts import render, get_object_or_404
from .models import Blog, CatalogOfArticles
from .get_blogs_in_category import *
   
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

# def catalog_name(request, pk):
#     blog = get_blogs_in_category()    
#     blogs = get_object_or_404(CatalogOfArticles, pk=pk)
#     return render(request, 'category.html', {
#         'blogs': blog[blogs.title],
#         'catalogs': count_blog_entries_by_catalog(),
#         'latest_publications': latest_publications(),
#         })

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .catalog_entry_counts import count_blog_entries_by_catalog  
from .latest_publications import latest_publications
from .models import Blog, CatalogOfArticles



from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def catalog_name(request, pk):
    catalog = get_object_or_404(CatalogOfArticles, pk=pk)
    blogs = get_blogs_in_category(catalog.title)  # Отримуємо блоги з даної категорії

    # Застосовуємо пагінацію
    paginator = Paginator(blogs, 30)  # Показуємо 10 блогів на сторінці
    page = request.GET.get('page')
    try:
        blogs_page = paginator.page(page)
    except PageNotAnInteger:
        # Якщо параметр сторінки не є цілим числом, показуємо першу сторінку
        blogs_page = paginator.page(1)
    except EmptyPage:
        # Якщо параметр сторінки виходить за межі, показуємо останню сторінку
        blogs_page = paginator.page(paginator.num_pages)
        
    return render(request, 'category.html', {
        'catalog': catalog,
        'blogs': blogs_page,  # Передаємо лише сторінку блогів, а не всі блоги
        'catalogs': count_blog_entries_by_catalog(),
        'latest_publications': latest_publications(),
    })
