from django.db import models
from day_2.apps.base_model import TimeStampedModel

class Sale(TimeStampedModel):
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.CASCADE,
        related_name='sale',
        verbose_name="Product"
    )

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    percent = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

