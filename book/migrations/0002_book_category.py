# Generated by Django 5.0.1 on 2024-03-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(default='', max_length=255),
        ),
    ]