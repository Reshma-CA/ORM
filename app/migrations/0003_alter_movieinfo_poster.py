# Generated by Django 4.2.8 on 2024-01-02 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_movieinfo_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='poster',
            field=models.ImageField(blank=True, upload_to='app/movies/'),
        ),
    ]
