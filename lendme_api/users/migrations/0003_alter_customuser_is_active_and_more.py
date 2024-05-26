# Generated by Django 4.2.13 on 2024-05-11 18:27

import django.contrib.auth.tokens
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='emailconfirmationtoken',
            name='token',
            field=models.CharField(default=django.contrib.auth.tokens.PasswordResetTokenGenerator.make_token, max_length=64),
        ),
    ]