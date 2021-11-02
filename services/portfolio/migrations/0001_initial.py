# Generated by Django 3.2.7 on 2021-09-18 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название категории услуги')),
                ('slug', models.SlugField(max_length=25, verbose_name='URL транслитом')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=21, verbose_name='Название услуги')),
                ('small_description', models.CharField(max_length=32, verbose_name='Краткое описание')),
                ('large_description', models.TextField(verbose_name='Полное описание')),
                ('small_image', models.ImageField(upload_to='static/portfolio', verbose_name='Маленькая картинка')),
                ('large_image', models.ImageField(upload_to='static/portfolio', verbose_name='Большая картинка')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.categorie', verbose_name='Категория услуги')),
            ],
            options={
                'verbose_name': 'Портфолио',
                'verbose_name_plural': 'Портфолио',
            },
        ),
    ]