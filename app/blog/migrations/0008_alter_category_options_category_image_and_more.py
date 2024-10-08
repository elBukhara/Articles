# Generated by Django 5.0.6 on 2024-07-31 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_tag_category_remove_article_tags_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default='default/category.jpg', null=True, upload_to='category_image'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
