# Generated by Django 4.2.4 on 2023-08-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Board",
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
                ("writer", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=500)),
                ("content", models.CharField(max_length=2000)),
                ("write_date", models.DateTimeField()),
            ],
        ),
    ]
