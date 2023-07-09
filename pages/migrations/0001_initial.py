# Generated by Django 4.2.2 on 2023-06-28 16:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='メニュー名')),
                ('img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='メニュー画像')),
                ('alt', models.CharField(max_length=100, verbose_name='画像タイトル')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('text', models.TextField(verbose_name='本文')),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像')),
                ('alt', models.CharField(max_length=100, verbose_name='画像タイトル')),
                ('category', models.CharField(choices=[('お店の紹介', 'お店の紹介'), ('期間限定メニュー', '期間限定メニュー'), ('イベント', 'イベント'), ('お客様との会話', 'お客様との会話')], max_length=100, verbose_name='カテゴリー')),
            ],
        ),
    ]
