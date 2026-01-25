from django.db import models
from enum import Enum
from apps.products.models import Product
from apps.users.models import User

class OrderStatus(Enum):
    PENDING = 'pending'
    PROCESSING = 'processing'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'
    
    @classmethod
    def choices(cls):
        return [(item.value, item.name.title()) for item in cls]

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, 
        default=OrderStatus.PENDING.value,
        choices=OrderStatus.choices()
    )
    
    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"