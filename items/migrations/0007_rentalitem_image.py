# Generated by Django 5.0.3 on 2024-05-05 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_remove_rentalitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='rental_item_images/'),
        ),
    ]