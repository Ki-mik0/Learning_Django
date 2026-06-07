from django.db import models
from apps.base_model import TimeStampedModel

class Category(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name = "Category name")
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
