# Generated by Django 4.1.3 on 2023-01-12 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("seller", "0004_alter_car_id"),
    ]

    operations = [
        migrations.RemoveField(model_name="car", name="car_insurance",),
        migrations.RemoveField(model_name="car", name="first_owner",),
    ]