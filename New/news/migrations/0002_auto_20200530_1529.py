# Generated by Django 3.0.5 on 2020-05-30 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='URL'),
        ),
    ]