# Generated by Django 2.2.6 on 2019-10-21 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twix', '0008_auto_20191019_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='is_personal',
            field=models.BooleanField(default=False),
        ),
    ]
