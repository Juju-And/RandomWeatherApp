# Generated by Django 5.1.4 on 2024-12-06 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Worldcities",
            fields=[
                ("city", models.TextField(blank=True, null=True)),
                ("lat", models.FloatField(blank=True, null=True)),
                ("lng", models.FloatField(blank=True, null=True)),
                ("country", models.TextField(blank=True, null=True)),
                (
                    "id",
                    models.IntegerField(blank=True, primary_key=True, serialize=False),
                ),
            ],
            options={
                "db_table": "worldcities",
                "managed": False,
            },
        ),
    ]
