from django.db import models
from ICC_Tracking.scripts import constants, autoassign

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

    orderID = models.CharField(max_length=50)
    assignedBearer = models.IntegerField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    orderStatus = models.IntegerField(choices=constants.O_STATUS_CHOICES, default=1)

    #Methods
    def assignBearerToCustomer(self):
        #Checking if bearer is already assigned
        if(self.assignedBearer is None):
            #If not assigned continue
            bearers = Bearer.objects.all()
            for bearer in bearers:
                print(bearer)      
        else:
            #Bearer Already Assigned
            print("Bearer already assigned")



    def __str__(self):
        return f'Customer : [{self.fname} {self.lname}] OrderID:[{self.orderID}] OrderStatus:[{self.orderStatus}] Assigned Bearer:[{self.assignedBearer}]'
    

class Bearer(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    assignedOrders = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    bearerStatus = models.IntegerField(choices=constants.B_STATUS_CHOICES, default=1)

    #Methods
    def __str__(self):
        return f'Bearer : [{self.name}], Assigned Orders : [{self.assignedOrders}], Current Location : [{self.location}]'
    