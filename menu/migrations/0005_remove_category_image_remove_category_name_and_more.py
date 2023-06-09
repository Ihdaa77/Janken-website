# Generated by Django 4.2.1 on 2023-05-26 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_remove_menu_size_itemsize_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='name_ar',
            field=models.CharField(default=0, max_length=100, verbose_name='Arabic Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(default=1, max_length=100, verbose_name='English Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='name_ar',
            field=models.CharField(default=0, max_length=100, verbose_name='Arabic Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='name_en',
            field=models.CharField(default=1, max_length=100, verbose_name='English Name'),
            preserve_default=False,
        ),
    ]
