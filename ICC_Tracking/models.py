from django.db import models
from django.db.models.enums import Choices
from ICC_Tracking.scripts import constants

# Create your models here.
class Customer(models.Model):
    
    ID = models.AutoField(primary_key=True)
    orderID = models.CharField(max_length=30, blank=True, unique=True)
    fname = models.CharField(max_length=50, default="Test")
    lname = models.CharField(max_length=50, default="Name")
    company = models.CharField(max_length=50, default="N/A")
    address = models.CharField(max_length=50, default="Test Address 11")
    area = models.IntegerField(choices=constants.LOCATIONS, default=1)
    time = models.IntegerField(choices=constants.TIME, default=1)
    optionalAddressInfo = models.CharField(max_length=50, default="N/A")
    city = models.CharField(max_length=50, default="Portmore")
    country = models.CharField(max_length=50, default="Jamaica")
    contactNumber = models.CharField(max_length=50, blank=True)
    contactEmail = models.EmailField(max_length=50, blank=True)

    assignedBearer = models.IntegerField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    orderStatus = models.IntegerField(choices=constants.O_STATUS_CHOICES, default=1)

    timeCreated = models.TimeField(auto_now_add=True)

    #Methods
    #Method to automatically assign customer to bearers or add them to the queue
    def assignBearerToCustomer(self):
        isset = False
        #Checking if bearer is already assigned
        if(self.assignedBearer is None or self.assignedBearer==-1):
            #If not assigned continue
            bearers = Bearer.objects.all()
            for bearer in bearers:
                if bearer.assignedOrders:
                    print(f'{bearer} already assigned at least 1 order : {bearer.assignedOrders}')
                else:
                    print(f'{bearer} not assigned, setting bearer')
                    self.assignedBearer = bearer.ID
                    orders = bearer.assignedOrders
                    print(orders)
                    bearer.assignedOrders = str(self.orderID)
                    bearer.save()
                    isset = True
                    break
        else:
            #Bearer Already Assigned
            isset = True
            print("Bearer already assigned in Customer")

        if isset :
            print(f'{self} has a bearer set')
        else:
            print(f'Could not set bearer for {self}, assigning -1 to add to queue')
            f = open("customerQueue.txt","a+")
            f.seek(0)
            if self.orderID in f.read().split(" "):
                print("Already in Queue")
            else:
                print("Enqueueing")
                self.assignedBearer = -1
                f.seek(0,2)
                f.write(f'{self.orderID} ')
            f.close()

    #Overriding default save function to automatically assign a bearer to a customer when a customer is created
    def save(self, *args, **kwargs):
        self.time = self.area
        self.assignBearerToCustomer()
        super(Customer, self).save(*args, **kwargs)

    #Overriding default delete function
    def delete(self, *args, **kwargs):
        print("Deleting")
        bearers = Bearer.objects.all()
        for bearer in bearers:
            if bearer.assignedOrders:
                print("Bearer has an order assigned")
                if bearer.assignedOrders.rstrip().lstrip() == self.orderID.rstrip().lstrip():
                    print("Matching Order ID detected")
                    bearer.assignedOrders = ""
                    bearer.save()
        return super(Customer, self).delete(*args, **kwargs)

    def __str__(self):
        return f'{self.fname} {self.lname}'
    

class Bearer(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    assignedOrders = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    bearerStatus = models.IntegerField(choices=constants.B_STATUS_CHOICES, default=1)

    #Methods
    def assignFromQueue(self):


        #Reading Queue File
        print("Reading Queue")
        f = open("customerQueue.txt","a+")
        f.seek(0)
        queue = f.read().split(" ")
        print(queue)
        #Adding Unqueued Customers
        customers = Customer.objects.all()
        for customer in customers:
            if customer.assignedBearer == -1 or customer.assignedBearer == None:
                print("No Duplicates Detected, Enqueing")
                f.seek(0,2)
                customer.assignedBearer == -1
                customer.save()
                f.write(f'{customer.orderID} ')

        f.close()

        if self.assignedOrders=="" or self.assignedOrders is None:
            print(f'No Orders Assigned to {self}')
            indx = -1
            for customer in queue:
                indx += 1
                try:
                    customerObj = Customer.objects.get(orderID=customer.rstrip().lstrip())
                    print(customerObj)
                    if customerObj is not None:
                        self.assignedOrders += customerObj.orderID
                        customerObj.assignedBearer = self.ID
                        print("Updating Customer")
                        customerObj.save()
                        queue.pop(indx)
                        f = open("customerQueue.txt","w")
                        for id in queue:
                            f.write(id+" ")
                        break
                except Exception as e:
                    print("Error", e)
                    print("Customer not found")
        else:
            print(f'Orders Already assigned to {self}')

    def checkForEmptyOrders(self):
        try:
            customer = Customer.objects.all().filter(assignedBearer=self.ID)[0]
            if customer:
                print("Matching Customer Found")
                self.assignedOrders = customer.orderID
        except Exception as e:
            print("Error in assignment", e)

    def save(self, *args, **kwargs):
        self.assignFromQueue()
        self.checkForEmptyOrders()
        super(Bearer, self).save(*args, **kwargs)

    #Overriding default delete function
    def delete(self, *args, **kwargs):
        print("Deleting")
        customers = Customer.objects.all()
        for customer in customers:
            if customer.orderID:
                print("Customer has an order assigned")
                if customer.orderID.rstrip().lstrip() == self.assignedOrders.rstrip().lstrip():
                    print("Matching Order ID detected")
                    customer.assignedBearer = -1
                    customer.save()
        return super(Bearer, self).delete(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
    