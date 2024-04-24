from .models import CatalogOfArticles, Blog

def get_blogs_in_category():
    all_blogs_in_category = {}
    for category in CatalogOfArticles.objects.all():
        all_blogs_in_category[category.title] = []

    for blogs in Blog.objects.all():
        if blogs.catalog_name in all_blogs_in_category:
            all_blogs_in_category[blogs.catalog_name].append(blogs)
        
    return all_blogs_in_category