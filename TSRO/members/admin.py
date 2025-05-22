from django.contrib import admin
from .models import DeliveryHistory

@admin.register(DeliveryHistory)
class DeliveryHistoryAdmin(admin.ModelAdmin):
    list_display = ('delivery_code', 'petroleum_name', 'supplier', 'date_deliver', 'total_volume', 'total_price', 'created_at')
    list_filter = ('supplier', 'date_deliver', 'petroleum_name')
    search_fields = ('delivery_code', 'petroleum_name', 'supplier')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-date_deliver',)
