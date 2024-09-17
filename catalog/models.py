from django.db import models, connection


class Product(models.Model):
    PRODUCT_CHOICES = (('ACTIVE', 'активный'), ('INACTIVE', 'неактивный'))

    name = models.CharField(
        max_length=150,
        verbose_name="Наименование товара",
        help_text="Введите наименование товара",
    )
    description = models.TextField(
        verbose_name="Описание товара",
        help_text="Введите описание товара",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="catalog/image",
        verbose_name="Изображение",
        help_text="Загрузите изображениеб",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        verbose_name="Категория", help_text="Укажите категорию"
    )
    price = models.IntegerField(
        verbose_name="Цена", help_text="Укажите цену", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    autor = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='автор', blank=True, null=True)
    is_published = models.CharField(max_length=20, choices=PRODUCT_CHOICES, default='INACTIVE',
                                    verbose_name='публикация')

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['id']
        permissions = [
            ("can_edit_is_published", "can edit is_published"),
            ("can_edit_description", "can edit description"),
            ("can_edit_category", "can edir category")
        ]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')


class Version(models.Model):
    product = models.ForeignKey(Product,
                                related_name="versions",
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                verbose_name='продукт'
                                )

    version_number = models.IntegerField(default=0, verbose_name='номер версии')
    version_name = models.TextField(verbose_name='название версии')
    version_indicator = models.BooleanField(default=True, verbose_name='актуалная версия')

    class Meta:
        verbose_name = 'Верссия'
        verbose_name_plural = 'Версии'

    def __str__(self):
        return self.version_name
