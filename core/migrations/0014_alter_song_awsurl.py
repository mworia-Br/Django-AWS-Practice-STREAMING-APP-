# Generated by Django 3.2.15 on 2022-09-29 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_song_awsurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='awsurl',
            field=models.CharField(default='add', max_length=1200, verbose_name='Player url'),
        ),
    ]
