from django.db import models
from users.models import CustomUser

class Stock(models.Model):
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    qty = models.IntegerField()
    operation = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.seller.username} - {self.product_id}'

class Price(models.Model):
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    seller_purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    seller_selling_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.seller.username} - {self.product_id}'
    
class Order(models.Model):
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=50)
    delivery_status = models.CharField(max_length=10)
    payment_type = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.seller.username} - {self.order_id}'
