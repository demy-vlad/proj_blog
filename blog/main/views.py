from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Blog, CatalogOfArticles
from django.db.models import Count

def index(request):
    catalogs = CatalogOfArticles.objects.annotate(blog_count=Count('blog'))
    latest_publications = Blog.objects.order_by('-created_at')[:10]
    return render(request, 'index.html', {
        'catalogs': catalogs,
        'latest_publications': latest_publications,
        })

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    catalog = get_object_or_404(CatalogOfArticles, title=blog.catalog_name)
    return render(request, 'blog_detail.html', {
        'catalog': catalog,
        'blog': blog,
    })

def catalog_name(request, slug):
    catalog = get_object_or_404(CatalogOfArticles, slug=slug)
    blogs = Blog.objects.filter(catalog_name=catalog.title)

    paginator = Paginator(blogs, 30)
    page = request.GET.get('page')
    try:
        blogs_page = paginator.page(page)
    except PageNotAnInteger:
        blogs_page = paginator.page(1)
    except EmptyPage:
        blogs_page = paginator.page(paginator.num_pages)
        
    return render(request, 'category.html', {
        'catalog': catalog,
        'blogs': blogs_page,
    })