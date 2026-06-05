from django.db import models
from day_2.apps.base_model import TimeStampedModel

class ProductImage(TimeStampedModel, models.Model):
    product = models.OneToOneField('product.Product', on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='products/%Y/%m/%d/')

    def __str__(self):
        return self.image.name
