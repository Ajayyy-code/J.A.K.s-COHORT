from django.contrib import admin
from django.db.models import fields

# Register your models here.
from .models import Customer, Order, Bearer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('ID','orderID','fname','lname','company','address','optionalAddressInfo','city','country','contactNumber','contactEmail')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('orderID','assignedCustomer','assignedBearer','subtotal','orderStatus')

class BearerAdmin(admin.ModelAdmin):
    list_display = ('ID','name','assignedOrders','location')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Bearer, BearerAdmin)