# Generated by Django 5.1.3 on 2024-11-15 18:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photos', '0002_alter_photo_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('date_time_of_publication', models.DateTimeField(auto_now_add=True)),
                ('to_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_comments', to='photos.photo')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_likes', to='photos.photo')),
            ],
        ),
    ]
