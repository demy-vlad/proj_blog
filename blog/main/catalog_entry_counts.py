from .models import CatalogOfArticles, Blog
from loguru import logger  

def count_blog_entries_by_catalog():
    catalog_entry_counts = {}  # Dictionary to store catalog entry counts
    for catalog in CatalogOfArticles.objects.all():
        if catalog.title not in catalog_entry_counts:
            catalog_entry_counts[catalog.title] = []  # Initialize an empty list for each catalog title
            # Count blog entries for the current catalog
            for blog in Blog.objects.all():
                if blog.catalog_name == catalog.title:
                    catalog_entry_counts[catalog.title].append(blog.catalog_name)  # Append blog catalog name to the list
            # Calculate the total count of blog entries for the current catalog
            entry_count = len(catalog_entry_counts[catalog.title])
            # Update the entry count in the dictionary
            catalog_entry_counts[catalog.title] = {
                'count': entry_count,
                'category': catalog.id,
            }
            logger.debug(catalog_entry_counts)
    return catalog_entry_counts