# Generated by Django 4.1.3 on 2022-12-31 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("seller", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="car_insurance",
            field=models.BooleanField(max_length=15),
        ),
    ]
