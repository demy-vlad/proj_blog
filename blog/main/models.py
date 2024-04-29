from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse
from slugify import slugify

class Users(models.Model):
    username = models.CharField("Username", max_length=20, null=False, blank=False)
    password = models.CharField("Password", max_length=100, null=False, blank=False)
    last_name = models.CharField("Last Name", max_length=50, null=False, blank=True, default='-')
    first_name = models.CharField("First Name", max_length=50, null=False, blank=True, default='-')
    date_birth = models.DateField("Date of Birth", null=False, blank=False)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

class CatalogOfArticles(models.Model):
    title = models.CharField("Title", max_length=200, null=False, blank=False)
    keywords_header = models.TextField("Keywords Header", max_length=300, null=False, blank=False)
    description_header = models.TextField("Description Header", max_length=300, null=False, blank=False)
    catalog_name = models.TextField("Catalog Name", max_length=100, null=False, blank=False)
    url_catalog = models.URLField("URL Catalog", max_length=1000, default='-')
    slug = models.SlugField("Slug", max_length=200, unique=True, null=True, blank=True)

    def generate_unique_slug(self):
        slug = slugify(self.title)
        counter = 1
        while CatalogOfArticles.objects.filter(slug=slug).exists():
            slug = f"{slugify(self.title)}-{counter}"
            counter += 1
        return slugify(slug)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('catalog_name', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = "Catalog of Article"
        verbose_name_plural = "Catalog of Articles"

    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField("Title", max_length=2000, null=False, blank=False)
    keywords_header = models.TextField("Keywords Header", max_length=2000, null=False, blank=False)
    description_header = models.TextField("Description Header", max_length=3000, null=False, blank=False)
    catalog_name = models.CharField("Catalog Name", max_length=100, null=False, blank=False)
    short_description = RichTextField("Short Description", max_length=6000, null=False, blank=False)
    full_description = RichTextField("Full Description", max_length=6000, null=False, blank=False)
    image = models.ImageField("Image", null=False, blank=False, default='default.png')
    date_added = models.DateField("Date Added", null=False, blank=False)
    slug = models.SlugField("Slug", max_length=200, unique=True, null=True, blank=True)
    flag = models.BooleanField("Moderation", default=False)
    
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title