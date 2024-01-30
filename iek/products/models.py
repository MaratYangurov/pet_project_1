from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()

class ProductCategory(models.Model):
    name_category = models.CharField(max_length=256, unique=True)
    description_category = models.TextField(null=True, blank=True)

class Product(models.Model):
    articl = models.CharField(max_length=128)
    description_product = models.TextField()
    i_nom = models.PositiveIntegerField()
    polus = models.PositiveIntegerField()
    current_time_curve = models.CharField(max_length=64)
    voltage_type = models.CharField(max_length=256)
    voltage_nom = models.PositiveIntegerField()
    i_cn = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(
        to=ProductCategory,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='product'
    )

    def __str__(self):
        return f'Модульный автомат. Артикл: {self.articl}'

