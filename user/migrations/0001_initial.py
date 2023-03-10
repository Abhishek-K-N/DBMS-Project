# Generated by Django 4.1.3 on 2023-01-07 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("seller", "0003_alter_car_car_insurance"),
    ]

    operations = [
        migrations.CreateModel(
            name="User_details",
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
                ("dob", models.DateField()),
                ("Address", models.CharField(max_length=100)),
                ("contact_number", models.CharField(max_length=14)),
                (
                    "cars_selled",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="seller.car"
                    ),
                ),
            ],
        ),
    ]
