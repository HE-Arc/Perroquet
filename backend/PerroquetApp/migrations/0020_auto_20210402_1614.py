# Generated by Django 3.1.7 on 2021-04-02 14:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PerroquetApp', '0019_auto_20210402_1509'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'message')},
        ),
    ]