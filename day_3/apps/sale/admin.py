from django.contrib import admin
from .models import Sale

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "quantity", "get_total_price", "created_at")
    list_filter = ("product", "created_at")

    @admin.display(description="Сума продажу")
    def get_total_price(self, obj):
        return obj.total_price