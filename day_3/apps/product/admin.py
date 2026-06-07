from django.contrib import admin
from apps.product.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", "created_at")
    list_filter = ("category", "created_at")

    @admin.display(description="Кількість товарів")
    def get_quantity(self, obj):
        return obj.quantity
