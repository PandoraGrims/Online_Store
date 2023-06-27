from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название")
    description = models.TextField(max_length=1000, verbose_name="Описание")

    def __str__(self):
        return f"{self.pk} {self.title}"

    class Meta:
        db_table = "category"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Good(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название")
    description = models.TextField(max_length=1000, verbose_name="Описание")
    category = models.ForeignKey("webapp.Category", on_delete=models.RESTRICT, verbose_name="Категория",
                                 related_name="categories", null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(null=True, blank=True, max_length=500)

    def __str__(self):
        return f"{self.pk} {self.title}"

    class Meta:
        db_table = "goods"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
