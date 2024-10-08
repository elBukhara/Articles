# Generated by Django 5.0.6 on 2024-07-27 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_image_article_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cover_image',
            field=models.ImageField(blank=True, default='default/cover.jpg', null=True, upload_to='cover_image'),
        ),
        migrations.AlterField(
            model_name='article',
            name='meta_description',
            field=models.TextField(default=''),
        ),
    ]
