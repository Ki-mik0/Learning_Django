from django.db import models

class Product(models.Model):
    category = models.ForeignKey(
        'category.Category',
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name="Категорія"
    )

    name = models.CharField(max_length=255, verbose_name="Product name")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL-address")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-created_at']

    def __str__(self):
        return self.name
