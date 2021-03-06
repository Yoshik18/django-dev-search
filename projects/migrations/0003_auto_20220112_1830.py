# Generated by Django 3.2.7 on 2022-01-12 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20211002_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='vote_ratio',
        ),
        migrations.RemoveField(
            model_name='review',
            name='vote_total',
        ),
        migrations.AddField(
            model_name='project',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='vote_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
