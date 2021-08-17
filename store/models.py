import uuid

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    reorder_level = models.IntegerField(default=5)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Reorder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product} {self.quantity} {self.processed}"