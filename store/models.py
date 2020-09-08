from django.db import models

# Create your models here.

class Product(models.Model):
    product_number = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=300,blank=True,null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return "%s"%self.product_number

class Customer(models.Model):
    customer_number = models.CharField(max_length=250,null=True,blank=True)
    first_name = models.CharField(max_length=250,null=True,blank=True)
    last_name = models.CharField(max_length=250,null=True,blank=True)
    email_id = models.CharField(max_length=250,null=True,blank=True)
    mobile_number = models.CharField(max_length=250,null=True,blank=True)
    address = models.CharField(max_length=250,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return "%s"%self.customer_number
    
class Order(models.Model):
    customer = models.ForeignKey(Customer)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    order_date = models.DateTimeField(auto_now_add=True,null=True)
    oder_status = models.BooleanField(default=True)
    billing_address = models.CharField(max_length=250)
    shipping_address = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True,null=True)

class Orderedproducts(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.CharField(max_length=250,null=True,blank=True)
    unit_price = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)

    def __str__(self):
        return "%s"%self.order_id


