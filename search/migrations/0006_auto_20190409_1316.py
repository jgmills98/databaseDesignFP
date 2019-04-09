# Generated by Django 2.2 on 2019-04-09 13:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20190409_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='search.Artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='label',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='album',
            name='sales',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='album',
            name='year',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='DOB',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='artist',
            name='Genre',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='artist',
            name='SSN',
            field=models.CharField(blank=True, max_length=9),
        ),
        migrations.AlterField(
            model_name='artist',
            name='label_rank',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='monthly_views',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='search.Album'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='search.Artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='featured',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='featured_artist', to='search.Artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='length',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='streams',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='track',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
