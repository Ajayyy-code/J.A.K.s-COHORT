from django.contrib import admin
from django.db.models import fields

# Register your models here.
from .models import Customer, Bearer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('ID','orderID','fname','lname','company','address','area','time','optionalAddressInfo','city','country','contactNumber','contactEmail','assignedBearer','subtotal','orderStatus')

class BearerAdmin(admin.ModelAdmin):
    list_display = ('ID','name','assignedOrders','location')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Bearer, BearerAdmin)