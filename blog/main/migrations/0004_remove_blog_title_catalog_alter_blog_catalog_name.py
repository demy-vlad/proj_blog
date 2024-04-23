# Generated by Django 5.0.4 on 2024-04-22 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_blog_description_header_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='title_catalog',
        ),
        migrations.AlterField(
            model_name='blog',
            name='catalog_name',
            field=models.CharField(max_length=100, verbose_name='Catalog Name'),
        ),
    ]
