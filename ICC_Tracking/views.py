from django.shortcuts import render

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
def inventory(request):
    return render(request, 'inventory.html')

#Admin Page
def admin(request):
    return render(request, 'admin.html')