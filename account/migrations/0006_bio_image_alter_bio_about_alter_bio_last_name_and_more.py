# Generated by Django 5.0.3 on 2024-05-07 15:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_bio_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='bio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
        migrations.AlterField(
            model_name='bio',
            name='about',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='bio',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bio',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bio',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bio',
            name='number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bio',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
