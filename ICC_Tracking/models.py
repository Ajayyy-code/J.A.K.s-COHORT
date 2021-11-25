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

    STATUS_CHOICES = (
       (1, "Active"),
        (2, "Delivered"),
    )
    orderID = models.CharField(max_length=50)
    assignedBearer = models.IntegerField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    orderStatus = models.IntegerField(choices=STATUS_CHOICES, default=1)

class Bearer(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    assignedOrders = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)