# Generated by Django 5.0.1 on 2024-01-18 18:48

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClothApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, max_length=250, null=True, unique=True)),
                ('image', models.ImageField(upload_to='img')),
                ('name', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('condition', models.CharField(choices=[('new', 'new'), ('old', 'old')], max_length=250)),
                ('information', models.TextField()),
                ('description', models.TextField()),
                ('stock', models.CharField(choices=[('in stock', 'in stock'), ('out stock', 'out stock')], max_length=200)),
                ('status', models.CharField(choices=[('published', 'published'), ('draft', 'draft')], max_length=250)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClothApp.categories')),
                ('filter_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClothApp.filter_price')),
            ],
        ),
    ]
