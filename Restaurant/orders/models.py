from django.db import models

# Create your models here.

class Order(models.Model):
    items = models.JSONField()  # Stores cart items as JSON
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    table_number = models.IntegerField(default=1)
    customer_name = models.CharField(max_length=100, default='Name')
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - ${self.total_price}"



class TableDetails(models.Model):
    table_number = models.IntegerField()
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Table {self.table_number} - {self.customer_name}"



