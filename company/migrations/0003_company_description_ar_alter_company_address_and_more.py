# Generated by Django 4.2.1 on 2023-05-26 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0002_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description_ar',
            field=models.TextField(default='', verbose_name='الوصف'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.TextField(max_length=1000, verbose_name='العنوان'),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(verbose_name='الوصف'),
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(max_length=200, verbose_name='البريد الالكتروني'),
        ),
        migrations.AlterField(
            model_name='company',
            name='fb_link',
            field=models.URLField(blank=True, null=True, verbose_name='رابط فيسبوك'),
        ),
        migrations.AlterField(
            model_name='company',
            name='ins_link',
            field=models.URLField(blank=True, null=True, verbose_name='رابط انستجرام'),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.URLField(blank=True, null=True, verbose_name='الموقع'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='company_logo/', verbose_name='الشعار'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=200, verbose_name='الاسم'),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(max_length=200, verbose_name='رقم الهاتف'),
        ),
        migrations.AlterField(
            model_name='company',
            name='sub_title',
            field=models.CharField(max_length=200, verbose_name='الاسم الفرعي'),
        ),
        migrations.AlterField(
            model_name='company',
            name='tw_link',
            field=models.URLField(blank=True, null=True, verbose_name='رابط تويتر'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='album/', verbose_name='الصورة'),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(max_length=200, verbose_name='رقم الهاتف'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='مستخدم'),
        ),
    ]