# Generated by Django 4.0.4 on 2022-08-01 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profil',
            options={'verbose_name_plural': 'Profiller'},
        ),
        migrations.AlterModelOptions(
            name='profildurum',
            options={'verbose_name_plural': 'Profil Durumu'},
        ),
        migrations.AlterField(
            model_name='profil',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='profil_fotolari/%Y/%m/%d/'),
        ),
    ]