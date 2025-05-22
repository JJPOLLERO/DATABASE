from django.db import models
from django.utils.timezone import now  

class DeliveryHistory(models.Model):
    petroleum_name = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)
    delivery_code = models.CharField(max_length=20, unique=True)
    date_deliver = models.DateField()
    total_volume = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.delivery_code} - {self.petroleum_name}"

    class Meta:
        verbose_name = "Delivery"
        verbose_name_plural = "Deliveries"
        ordering = ['-date_deliver']