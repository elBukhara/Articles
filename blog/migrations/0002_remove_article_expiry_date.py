# Generated by Django 5.0.6 on 2024-06-24 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='expiry_date',
        ),
    ]
