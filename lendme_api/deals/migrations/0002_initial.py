# Generated by Django 4.2.8 on 2024-05-03 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("deals", "0001_initial"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="deals",
            name="confirm_deposite",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="deals",
                to="products.deposite",
                verbose_name="Подтвержденный депозит",
            ),
        ),
        migrations.AddField(
            model_name="deals",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="deals",
                to="products.product",
                verbose_name="Продукт",
            ),
        ),
    ]
