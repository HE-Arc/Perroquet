# Generated by Django 3.1.7 on 2021-03-19 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PerroquetApp', '0007_auto_20210315_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]