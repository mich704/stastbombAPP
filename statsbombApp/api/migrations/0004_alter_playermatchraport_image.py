# Generated by Django 4.0.1 on 2023-04-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_playermatchraport_match_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playermatchraport',
            name='image',
            field=models.ImageField(upload_to='statsbombApp/frontend/public'),
        ),
    ]
