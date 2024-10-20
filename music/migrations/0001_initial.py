# Generated by Django 5.0.7 on 2024-07-14 09:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Singer",
            fields=[
                (
                    "singer_id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("singer_name", models.CharField(max_length=100)),
                ("summ", models.TextField()),
                ("original_url", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Song",
            fields=[
                (
                    "song_id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=100)),
                ("lyrics", models.TextField()),
                ("original_url", models.URLField()),
                (
                    "singer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="music.singer"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "song",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="music.song"
                    ),
                ),
            ],
        ),
    ]
