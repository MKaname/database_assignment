# Generated by Django 3.1 on 2020-08-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='page',
        ),
        migrations.AddField(
            model_name='book',
            name='number',
            field=models.IntegerField(blank=True, default=0, verbose_name='巻数'),
        ),
    ]
