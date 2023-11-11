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
    serv = part.objects.all()
    ser_context = {
        "serv1": serv,
    }
    return render(request, 'pages/portfolio-details.html', ser_context)

# def penu_list(request,listing_id):
#     serv = part.objects.all()
#     ser_context = {
#         "serv1": serv,
#     }
#     return render(request, 'pages/penu.html', ser_context)

# def hydr_list(request, listing_id):
#     serv = part.objects.all()
#     ser_context = {
#         "serv1": serv,
#     }
#     return render(request, 'pages/hydro.html',ser_context)