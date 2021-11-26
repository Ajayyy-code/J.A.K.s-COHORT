from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
# request -> response
# Each view needs to be mapped to a url

#render takes in a request, template, context
#Pass variables to the templates using a dictionary as context
#Syntax for accessing variables in templates {{var}}
#Syntax for control structures in templates {% if condition %}

#Landing Page
def index(request):
    return render(request, 'index.html')

#Inventory Page
@staff_member_required()
def inventory(request):
    return render(request, 'inventory.html')

#Admin Page
@staff_member_required()
def admin(request):
    return render(request, 'admin.html')