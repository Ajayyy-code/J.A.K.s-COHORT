from django.db import models
from ICC_Tracking.scripts import constants

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

    assignedBearer = models.IntegerField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    orderStatus = models.IntegerField(choices=constants.O_STATUS_CHOICES, default=1)

    #Methods
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
                    bearer.assignedOrders = str(orders) + str(self.orderID)
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
                self.assignedBearer = -1
            else:
                print("Enqueueing")
                self.assignedBearer = -1
                f.seek(0,2)
                f.write(f'{self.orderID} ')
            f.close()

    #Overriding default save function to automatically assign a bearer to a customer when a customer is created
    def save(self, *args, **kwargs):
        self.assignBearerToCustomer()
        super(Customer, self).save(*args, **kwargs)

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
        print("Reading Queue")
        f = open("customerQueue.txt","a+")
        f.seek(0)
        queue = f.read().split(" ")
        print(queue)
        f.close()

        if self.assignedOrders=="" or self.assignedOrders is None:
            print(f'No Orders Assigned to {self}')
            indx = -1
            for customer in queue:
                indx += 1
                try:
                    customerObj = Customer.objects.get(orderID=customer)
                    print(customerObj)
                    if customerObj is not None:
                        self.assignedOrders += customerObj.orderID+" "
                        queue.pop(indx)
                        f = open("customerQueue.txt","w")
                        for id in queue:
                            f.write(id+" ")
                        break
                except:
                    print("Customer not found")
        else:
            print(f'Orders Already assigned to {self}')


    def save(self, *args, **kwargs):
        self.assignFromQueue()
        super(Bearer, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
    