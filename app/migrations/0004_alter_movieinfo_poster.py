# Generated by Django 4.2.8 on 2024-01-02 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_movieinfo_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='poster',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
