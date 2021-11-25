from django.db import models

# Create your models here.
class Customer(models.Model):
    ID = models.AutoField(primary_key=True)
    orderID = models.CharField(max_length=30, blank=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    company = models.CharField(max_length=50, default="N/A")
    address = models.CharField(max_length=50)
    optionalAddressInfo = models.CharField(max_length=50, default="N/A")
    city = models.CharField(max_length=50, default="Portmore")
    country = models.CharField(max_length=50, default="Jamaica")
    contactNumber = models.CharField(max_length=50, blank=True)
    contactEmail = models.EmailField(max_length=50, blank=True)

class Order(models.Model):

    STATUS_CHOICES = (
       (1, "Preparing"),
       (2, "Active"),
        (3, "Delivered"),
    )

    orderID = models.CharField(max_length=50, primary_key=True)
    assignedCustomer = models.IntegerField()
    assignedBearer = models.IntegerField(blank=True)
    subtotal = models.FloatField(blank=True)
    orderStatus = models.IntegerField(choices=STATUS_CHOICES, default=1)

class Bearer(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    assignedOrders = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)