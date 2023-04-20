# Generated by Django 4.0.1 on 2023-04-20 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playermatchraport',
            name='match',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, parent_link=True, to='api.match'),
        ),
        migrations.AlterField(
            model_name='playermatchraport',
            name='player',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, parent_link=True, to='api.player'),
        ),
    ]