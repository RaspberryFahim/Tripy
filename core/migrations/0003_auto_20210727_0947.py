# Generated by Django 3.2.5 on 2021-07-27 09:47

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210727_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='phone',
            field=models.CharField(blank=True, max_length=63, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.upload_to),
        ),
    ]
