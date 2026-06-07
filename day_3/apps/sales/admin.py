from django.contrib import admin
from .models import Sales

@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "quantity", "created_at")
    list_filter = ("product", "created_at")

    @admin.display(description="Кількість продажів")
    def get_quantity(self, obj):
        return obj.quantity