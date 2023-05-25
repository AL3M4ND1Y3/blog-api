# Generated by Django 4.2 on 2023-05-20 00:25

import apps.blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('thumnail', models.ImageField(blank=True, null=True, upload_to=apps.blog.models.user_directory_path)),
                ('video', models.FileField(blank=True, null=True, upload_to=apps.blog.models.user_directory_path)),
                ('exerpt', models.TextField(null=True)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=250, unique=True, unique_for_date='published')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('published',),
            },
        ),
    ]