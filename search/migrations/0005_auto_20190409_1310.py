# Generated by Django 2.2 on 2019-04-09 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20190409_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
