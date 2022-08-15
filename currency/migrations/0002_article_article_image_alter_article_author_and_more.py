# Generated by Django 4.0.3 on 2022-03-07 01:10

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Makaleye Resim Ekleyin'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='currency',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Başlık'),
        ),
    ]