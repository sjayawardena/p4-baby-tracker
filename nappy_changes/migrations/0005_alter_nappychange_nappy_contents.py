# Generated by Django 4.2.11 on 2024-04-07 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nappy_changes", "0004_alter_nappychange_nappy_contents"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nappychange",
            name="nappy_contents",
            field=models.CharField(
                choices=[
                    ("wet", "Wet"),
                    ("dirty", "Dirty"),
                    ("wet+dirty", "Wet+Dirty"),
                    ("nothing", "Nothing"),
                ],
                max_length=20,
            ),
        ),
    ]