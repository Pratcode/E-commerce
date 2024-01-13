from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_img = models.ImageField(null=True)
    product_price = models.FloatField()
    product_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    user_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product_item = models.ForeignKey(Product, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    order_date = models.DateTimeField(auto_now_add=True, null=True)
    payment = models.CharField(max_length=100, null=True)


