# Generated by Django 4.0.1 on 2023-04-06 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_match_away_lineup_match_home_lineup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lineup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.IntegerField()),
                ('team_id', models.IntegerField()),
                ('team_name', models.CharField(max_length=20)),
                ('players', models.ManyToManyField(to='api.Player')),
            ],
        ),
        migrations.AlterField(
            model_name='match',
            name='away_lineup',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='away_lineup', to='api.lineup'),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_lineup',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_lineup', to='api.lineup'),
        ),
    ]