# Generated by Django 2.2.6 on 2019-10-19 11:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twix', '0005_auto_20191019_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(related_name='twix_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]
