from .models import CatalogOfArticles, Blog

def get_blogs():
    all_blogs_in_category = {}
    for category in CatalogOfArticles.objects.all():
        all_blogs_in_category[category.title] = []

    for blogs in Blog.objects.all():
        if blogs.catalog_name in all_blogs_in_category:
            all_blogs_in_category[blogs.catalog_name].append(blogs)
        
    return all_blogs_in_category

def get_blogs_in_category(category_name):
    blogs_in_category = Blog.objects.filter(catalog_name=category_name)
    return blogs_in_category