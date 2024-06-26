from django import forms
from .models import Users, CatalogOfArticles, Blog

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password', 'last_name', 'first_name', 'date_birth']
        labels = {
            'username': 'Username',
            'password': 'Password',
            'last_name': 'Last Name',
            'first_name': 'First Name',
            'date_birth': 'Date of Birth',
        }

class CatalogOfArticlesForm(forms.ModelForm):
    class Meta:
        model = CatalogOfArticles
        fields = ['title', 'keywords_header', 'description_header', 'catalog_name', 'url_catalog', 'slug']
        labels = {
            'title': 'Title',
            'keywords_header': 'Keywords Header',
            'description_header': 'Description Header',
            'catalog_name': 'Catalog Name',
            'url_catalog': 'URL Catalog',
            'slug': "Slug",
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'keywords_header', 'description_header', 'short_description', 'full_description', 'image', 'date_added', 'catalog_name', 'slug']
        labels = {
            'title': 'Title',
            'keywords_header': 'Keywords Header',
            'description_header': 'Description Header',
            'catalog_name': 'Catalog Name',
            'short_description': 'Short Description',
            'full_description': 'Full Description',
            'image': 'Image',
            'date_added': 'Date Added',
            'slug': 'Slug'
        }