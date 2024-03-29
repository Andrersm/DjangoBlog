# Generated by Django 5.0.1 on 2024-01-22 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_page_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, default=None, null=True, unique=True)),
                ('excerpt', models.CharField(max_length=255)),
                ('is_published', models.BooleanField(default=False, help_text='Este campo precisará estar                                       marcado para o post ser exibida')),
                ('content', models.TextField()),
                ('cover', models.ImageField(blank=True, default='', upload_to='posts/%Y/%m/')),
                ('cover_in_post_content', models.BooleanField(default=True, help_text='exibir o cover?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
                ('tags', models.ManyToManyField(blank=True, default='', to='blog.tag')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
