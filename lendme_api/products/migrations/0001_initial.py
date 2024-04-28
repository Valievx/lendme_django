# Generated by Django 4.2.8 on 2024-04-28 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                (
                    "address",
                    models.CharField(default="Заглушка адреса", max_length=255),
                ),
                ("city", models.CharField(default="Заглушка города", max_length=100)),
                ("metro", models.CharField(default="Заглушка метро", max_length=100)),
            ],
            options={
                "verbose_name": "Адрес",
                "verbose_name_plural": "Адреса",
                "ordering": ("city",),
            },
        ),
        migrations.CreateModel(
            name="Category",
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
                (
                    "title",
                    models.CharField(
                        max_length=35,
                        unique=True,
                        verbose_name="Наименование категории",
                    ),
                ),
                ("slug", models.SlugField(max_length=35, verbose_name="Ссылка")),
            ],
        ),
        migrations.CreateModel(
            name="Deposite",
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
                (
                    "title",
                    models.CharField(
                        max_length=35, verbose_name="Наименование депозита"
                    ),
                ),
                ("slug", models.SlugField(max_length=35, verbose_name="Ссылка")),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=100, verbose_name="Название")),
                ("description", models.TextField(verbose_name="Описание")),
                ("price", models.IntegerField(verbose_name="Цена")),
                ("image", models.ImageField(upload_to="products/image_products")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата публикации"
                    ),
                ),
                (
                    "time_period",
                    models.CharField(
                        choices=[
                            ("Час", "Час"),
                            ("Сутки", "Сутки"),
                            ("Месяц", "Месяц"),
                        ],
                        max_length=20,
                        verbose_name="Период времени",
                    ),
                ),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="products.address",
                        verbose_name="Адрес",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubCategory1",
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
                (
                    "title",
                    models.CharField(
                        max_length=35, verbose_name="Наименование подкатегории"
                    ),
                ),
                ("slug", models.SlugField(max_length=35, verbose_name="Ссылка")),
            ],
        ),
        migrations.CreateModel(
            name="SubCategory2",
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
                (
                    "title",
                    models.CharField(
                        max_length=35, verbose_name="Наименование подкатегории"
                    ),
                ),
                ("slug", models.SlugField(max_length=35, verbose_name="Ссылка")),
            ],
        ),
        migrations.CreateModel(
            name="ProductImages",
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
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="products.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductDeposite",
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
                (
                    "value",
                    models.IntegerField(
                        blank=True, default=0, verbose_name="Сумма депозита"
                    ),
                ),
                (
                    "deposit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products_deposite",
                        to="products.deposite",
                        verbose_name="Депозит",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products_deposite",
                        to="products.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
        ),
    ]
