from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.

def aplikacioni(request):
    
    trade = Trade.objects.all()
    context ={"trade":trade}
    return render(request, 'aplikacioni.html', context)

def contact(request):
    
    
    if request.method == "POST":
        name_contact = request.POST["firstName"]
        surname_contact = request.POST["lastName"]
        email_contact = request.POST["email"]
        message_contact = request.POST["message"]
        number_contact = request.POST["number"]

        Contact(contact_name=name_contact, contact_surname=surname_contact, 
        contact_email = email_contact,contact_number = number_contact, contact_textarea=message_contact).save()
        return render(request, 'response.html')
    return render(request, 'contact.html')
    
def aboutus(request):
    return render(request, 'aboutus.html')