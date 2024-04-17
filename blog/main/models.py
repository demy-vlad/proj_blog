from django.db import models

class Users(models.Model):
    username = models.CharField("Username", max_length=20, null=False, blank=False)
    password = models.CharField("Password", max_length=100, null=False, blank=False)
    last_name = models.CharField("Last Name", max_length=50, null=False, blank=True, default='-')
    first_name = models.CharField("First Name", max_length=50, null=False, blank=True, default='-')
    date_birth = models.DateField("Date of Birth", null=False, blank=False)

    class Meta:
        verbose_name_plural = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

class CatalogOfArticles(models.Model):
    title = models.CharField("Title", max_length=200, null=False, blank=False)
    keywords_header = models.CharField("Keywords Header", max_length=300, null=False, blank=False)
    description_header = models.CharField("Description Header", max_length=300, null=False, blank=False)
    catalog_name = models.CharField("Catalog Name", max_length=100, null=False, blank=False)
    description = models.TextField("Description", null=False, blank=False)

    class Meta:
        verbose_name_plural = "Catalog of Article"
        verbose_name_plural = "Catalog of Articles"

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField("Title", max_length=200, null=False, blank=False)
    keywords_header = models.CharField("Keywords Header", max_length=300, null=False, blank=False)
    description_header = models.CharField("Description Header", max_length=300, null=False, blank=False)
    catalog_name = models.CharField("Catalog Name", max_length=100, null=False, blank=False)
    short_description = models.CharField("Short Description", max_length=400, null=False, blank=False)
    full_description = models.CharField("Full Description", max_length=400, null=False, blank=False)
    image = models.ImageField("Image", null=False, blank=False, default='default.jpg')
    date_added = models.DateField("Date Added", null=False, blank=False)

    class Meta:
        verbose_name_plural = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title