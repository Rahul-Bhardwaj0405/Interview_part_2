from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[("PENDING", "pending"), ("PAID", "Paid")])
    created_at = models.DateField(auto_now_add=True)