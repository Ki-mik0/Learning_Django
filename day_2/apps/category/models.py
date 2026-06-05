from django.db import models
from day_2.apps.base_model import TimeStampedModel

class Category(TimeStampedModel, models.Model):
    name = models.CharField(max_length=255, verbose_name = "Category name")
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
