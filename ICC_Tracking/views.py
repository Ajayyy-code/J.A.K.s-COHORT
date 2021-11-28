from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail

from ICC_Tracking.models import Bearer, Customer
from ICC_Tracking.scripts import constants

# Create your views here.
# request -> response
# Each view needs to be mapped to a url

#render takes in a request, template, context
#Pass variables to the templates using a dictionary as context
#Syntax for accessing variables in templates {{var}}
#Syntax for control structures in templates {% if condition %}

#Landing Page
def index(request):
    # Checks if there is a post request on the webpage, and collects the name of the person,email and feedback they have written
    if request.method == "POST":

        if 'fBtn' in request.POST:

            message_name =  request.POST['realname']
            message_email = request.POST['email']
            message = request.POST['comments']

            if message_name != "" or message_email != "" or message != "":

                #Sends email with feedback to the owner/business
                send_mail( 'Feedback from '+ message_name,message + '\n Customer email: ' + message_email, message_email,['icecc.feedback@gmail.com'])
                #Sends confirmation email to the customer
                send_mail('Feedback received', 'Thank you for the feedback','icecc.feedback@gmail.com', [message_email])

                return render(request,'index.html',{'message_name':message_name})
            else:
                return render(request, 'index.html')

        elif 'sBtn' in request.POST:

            orderID = request.POST['tInput']
            customers = Customer.objects.all()

            for customer in customers:
                if customer.orderID == orderID:
                    try:
                        bearer = Bearer.objects.all().filter(ID=customer.assignedBearer)[0]
                        area = constants.List_LOCATIONS[customer.area-1]
                    except IndexError:
                        bearer = None
                        area = None
                    return render(request,'index.html',{"customer": customer, "bearer":bearer, "area":area})
            
            return render(request,'index.html')

    return render(request,'index.html')

    





#Inventory Page
@staff_member_required()
def inventory(request):
    bearers = Bearer.objects.all()
    return render(request, 'inventory.html', {'bearers':bearers})

#Admin Page
@staff_member_required()
def admin(request):
    return render(request, 'admin.html')

