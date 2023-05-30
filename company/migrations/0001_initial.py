# Generated by Django 4.2.1 on 2023-05-24 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('sub_title', models.CharField(max_length=200, verbose_name='Sub titl')),
                ('description', models.TextField(verbose_name='Description')),
                ('address', models.TextField(max_length=1000, verbose_name='Address')),
                ('phone', models.CharField(max_length=200, verbose_name='Phone')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company_logo/', verbose_name='Logo')),
                ('location', models.URLField(blank=True, null=True, verbose_name='location')),
                ('fb_link', models.URLField(blank=True, null=True, verbose_name='facebook link')),
                ('ins_link', models.URLField(blank=True, null=True, verbose_name='instagram link')),
                ('tw_link', models.URLField(blank=True, null=True, verbose_name='tweeter link')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=200, verbose_name='Phone')),
                ('city', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
