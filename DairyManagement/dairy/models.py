from django.db import models
from django.contrib.auth.models import User


# 🧈 Product model — stores all dairy products
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


# 🛒 Order model — stores customer orders
class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
    ]
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"

    def get_total(self):
        """Calculate total order amount"""
        return sum(item.get_subtotal() for item in self.items.all())

    class Meta:
        ordering = ['-created_at']


# 🧾 Order Item model — connects products to orders
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x {self.product.name}"

    def get_subtotal(self):
        return self.quantity * self.price


# 🥛 Milk Record model — (optional) tracks daily milk production
class MilkRecord(models.Model):
    cow_id = models.CharField(max_length=50)
    date = models.DateField()
    milk_quantity = models.FloatField(help_text="Litres of milk produced")
    fat_content = models.FloatField(null=True, blank=True, help_text="Fat percentage")
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cow {self.cow_id} - {self.date}"

    class Meta:
        ordering = ['-date']
