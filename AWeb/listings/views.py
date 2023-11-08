from django.shortcuts import render
from .models import part
# Create your views here.

def listings(request):
    serv = part.objects.all()
    ser_context = {
        "serv1": serv,
    }
    return render(request, 'pages/listings.html', ser_context)

def listing(request,listing_id):
    return render(request, 'pages/portfolio-details.html')

def penu_list(request):

    return render(request, 'pages/penu.html')

def hydr_list(request):
    serv = part.objects.all()
    ser_context = {
        "serv1": serv,
    }
    return render(request, 'pages/heyd.html')