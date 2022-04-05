from django.shortcuts import render
from django.contrib import messages
from .models import addService

# Create your views here.

def services(request): 
    allServices = addService.objects.all()
    context = {'allServices': allServices}
    return render(request, "services/services.html",context)

def addServices(request): 
    if request.method == "POST":
        Title = request.POST['ServiceTitle']
        Author = request.POST['Author']
        Description = request.POST['Description']
        Code = request.POST['Code']
        addServiceData = addService(title=Title, author=Author, description=Description,code=Code)
        addServiceData.save()
        messages.success(
            request, "Your new service has been successfully added")
    return render(request, "services/addServices.html")