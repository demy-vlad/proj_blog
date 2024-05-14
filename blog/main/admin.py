import os
from django.contrib import admin

from web_scraping.web_scraping_ek import BlogScraper
from .models import Users, CatalogOfArticles, Blog
from .forms import UsersForm, CatalogOfArticlesForm, BlogForm

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    form = UsersForm
    list_display = ['username', 'last_name', 'first_name', 'date_birth']
    search_fields = ['username', 'last_name', 'first_name']
    list_filter = ['date_birth']

@admin.register(CatalogOfArticles)
class CatalogOfArticlesAdmin(admin.ModelAdmin):
    form = CatalogOfArticlesForm
    list_display = ['title', 'catalog_name']
    search_fields = ['title', 'catalog_name']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogForm
    list_display = ['title', 'catalog_name', 'date_added', 'flag']
    search_fields = ['title', 'catalog_name']
    list_filter = ['flag', 'catalog_name']
    actions = ['run_web_scraping']  # Здесь добавляем ваше действие

    def run_web_scraping(self, request, queryset):
        self.message_user(request, "Web scraping executed successfully.")
        BlogScraper().get_all_catalogs()
        
    run_web_scraping.short_description = "Run web scraping"