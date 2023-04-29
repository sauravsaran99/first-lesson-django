from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    #sendig variable
    context = {
        "variable": "this is sent", 
        "variable2": "I am great"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")

def contact(request):
    if request.method == "POST":
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        contact = Contact(email=email, phone=phone, password=password, date=datetime.today())
        contact.save()
        messages.success(request, 'Your data has saved')
    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")