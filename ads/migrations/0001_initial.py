# Generated by Django 4.1.3 on 2022-11-22 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=2000)),
                ('image', models.ImageField(upload_to='images/')),
                ('is_published', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=100)),
                ('lat', models.FloatField(null=True)),
                ('lng', models.FloatField(null=True)),
            ],
            options={
                'verbose_name': 'Местоположение',
                'verbose_name_plural': 'Местоположения',
            },
        ),
    ]
