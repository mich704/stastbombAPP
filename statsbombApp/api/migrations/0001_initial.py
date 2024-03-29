# Generated by Django 4.0.1 on 2023-04-20 15:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('competition_id', models.IntegerField(primary_key=True, serialize=False)),
                ('season_name', models.CharField(max_length=10)),
                ('competition_name', models.CharField(max_length=20)),
                ('season_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Lineup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.IntegerField()),
                ('team_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('match_id', models.IntegerField(primary_key=True, serialize=False)),
                ('home_team', models.CharField(max_length=20)),
                ('away_team', models.CharField(max_length=20)),
                ('home_score', models.IntegerField()),
                ('away_score', models.IntegerField()),
                ('away_lineup', models.OneToOneField(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='away_lineup', to='api.lineup')),
                ('competition', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='api.competition')),
                ('home_lineup', models.OneToOneField(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_lineup', to='api.lineup')),
            ],
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, parent_link=True, to='api.event')),
                ('location_start_X', models.FloatField(default=-1)),
                ('location_start_Y', models.FloatField(default=-1)),
                ('pass_end_location_X', models.FloatField(default=-1)),
                ('pass_end_location_Y', models.FloatField(default=-1)),
                ('pass_outcome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.IntegerField(primary_key=True, serialize=False)),
                ('player', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('season_id', models.IntegerField(primary_key=True, serialize=False)),
                ('season_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerMatchRaport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raport_type', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='media')),
                ('match', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.match')),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.player')),
            ],
        ),
        migrations.AddField(
            model_name='lineup',
            name='players',
            field=models.ManyToManyField(to='api.Player'),
        ),
        migrations.AddField(
            model_name='event',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.match'),
        ),
        migrations.AddField(
            model_name='event',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.player'),
        ),
    ]
