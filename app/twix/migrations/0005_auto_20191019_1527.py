# Generated by Django 2.2.6 on 2019-10-19 10:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twix', '0004_auto_20191019_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='twix_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]