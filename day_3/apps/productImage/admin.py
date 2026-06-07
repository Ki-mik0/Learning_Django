from django.contrib import admin
from apps.productImage.models import ProductImage

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "image")
    list_filter = ("product",)


