# Generated by Django 5.0.6 on 2024-07-26 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_article_expiry_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-publish_date']},
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='cover_image'),
        ),
    ]