# Generated by Django 4.0 on 2022-03-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0004_rename_kid_food_image_kid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_image',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
