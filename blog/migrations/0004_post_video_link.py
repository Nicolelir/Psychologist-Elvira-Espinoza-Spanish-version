# Generated by Django 4.2.11 on 2025-01-18 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video_link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]