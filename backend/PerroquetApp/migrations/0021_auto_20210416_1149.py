# Generated by Django 3.1.7 on 2021-04-16 09:49

import PerroquetApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PerroquetApp', '0020_auto_20210402_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default=PerroquetApp.models.get_random_default_pp, null=True, upload_to='img/%Y/%m/%d/'),
        ),
    ]
