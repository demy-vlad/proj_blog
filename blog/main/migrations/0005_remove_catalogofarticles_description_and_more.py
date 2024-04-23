# Generated by Django 5.0.4 on 2024-04-22 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_blog_title_catalog_alter_blog_catalog_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogofarticles',
            name='description',
        ),
        migrations.AlterField(
            model_name='blog',
            name='catalog_name',
            field=models.TextField(max_length=100, verbose_name='Catalog Name'),
        ),
    ]
