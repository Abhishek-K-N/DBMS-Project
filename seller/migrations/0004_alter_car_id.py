# Generated by Django 4.1.3 on 2023-01-07 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("seller", "0003_alter_car_car_insurance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]