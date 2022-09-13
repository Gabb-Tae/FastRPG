# Generated by Django 4.1.1 on 2022-09-13 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="itens",
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
                ("description", models.CharField(max_length=100)),
                ("damage", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="rpgclass",
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
                ("name", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=700)),
                ("life", models.IntegerField(max_length=5)),
                ("main_skill", models.CharField(max_length=20)),
                ("strength", models.IntegerField(max_length=2)),
                ("dexterity", models.IntegerField(max_length=2)),
                ("constitution", models.IntegerField(max_length=2)),
                ("intelligence", models.IntegerField(max_length=2)),
                ("wisdom", models.IntegerField(max_length=2)),
                ("charism", models.IntegerField(max_length=2)),
            ],
            options={
                "verbose_name_plural": "Classes",
            },
        ),
        migrations.CreateModel(
            name="rpgrace",
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
                ("name", models.CharField(max_length=50)),
                ("features", models.CharField(max_length=700)),
                ("life", models.IntegerField(max_length=5)),
                ("size", models.CharField(max_length=20)),
                ("speed", models.CharField(max_length=20)),
                ("languages", models.CharField(max_length=60)),
                ("strength", models.IntegerField(max_length=2)),
                ("dexterity", models.IntegerField(max_length=2)),
                ("constitution", models.IntegerField(max_length=2)),
                ("intelligence", models.IntegerField(max_length=2)),
                ("wisdom", models.IntegerField(max_length=2)),
                ("charism", models.IntegerField(max_length=2)),
            ],
            options={
                "verbose_name_plural": "Raças",
            },
        ),
        migrations.CreateModel(
            name="skills",
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
                ("description", models.CharField(max_length=1000)),
                (
                    "rpgclass",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="skills",
                        to="core.rpgclass",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="itensclass",
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
                (
                    "itens",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="itensclass",
                        to="core.itens",
                    ),
                ),
                (
                    "rpgclass",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="itensclass",
                        to="core.rpgclass",
                    ),
                ),
            ],
        ),
    ]
