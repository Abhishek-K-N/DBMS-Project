# Generated by Django 4.1.3 on 2023-01-07 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("seller", "0002_alter_car_car_insurance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car", name="car_insurance", field=models.BooleanField(),
        ),
    ]
