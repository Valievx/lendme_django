# Generated by Django 4.2.8 on 2024-05-23 16:57

import django.contrib.auth.tokens
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_customuser_is_active_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailconfirmationtoken",
            name="token",
            field=models.CharField(
                default=django.contrib.auth.tokens.PasswordResetTokenGenerator.make_token,
                max_length=64,
            ),
        ),
    ]