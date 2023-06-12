# Generated by Django 4.2.2 on 2023-06-12 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("groups", "0001_initial"),
        ("traits", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pet",
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
                ("age", models.IntegerField()),
                ("weight", models.FloatField()),
                (
                    "sex",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Not Informed.", "Default"),
                            ("Female", "Female"),
                        ],
                        default="Not Informed.",
                        max_length=20,
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="groups.group",
                    ),
                ),
                (
                    "traits",
                    models.ManyToManyField(
                        null=True, related_name="pets", to="traits.trait"
                    ),
                ),
            ],
        ),
    ]
