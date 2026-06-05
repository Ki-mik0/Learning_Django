from django.db import models
from apps.base_model import TimeStampedModel

class Tag(TimeStampedModel):
    product = models.ManyToManyField('product.Product', related_name='tags')
    category = models.ManyToManyField('category.Category', related_name='tags')

    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name