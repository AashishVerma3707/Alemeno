# Generated by Django 4.0 on 2022-03-27 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Food_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('Created_on', models.DateField(auto_now_add=True)),
                ('Updated_om', models.DateField(auto_now=True)),
                ('Is_approved', models.BooleanField(default=False)),
                ('Approved_by', models.CharField(max_length=20)),
                ('Food_group', models.CharField(choices=[('Veg', 'Veg'), ('Fruit', 'Fruit'), ('Grain', 'Grain'), ('Protein', 'Protein'), ('Dairy', 'Dairy'), ('Confectionery', 'Confectionery'), ('Unknown', 'Unknown')], default='Assigned', max_length=30)),
                ('Kid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.kid')),
            ],
        ),
    ]
