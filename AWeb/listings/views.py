from django.shortcuts import get_object_or_404, render
from .models import metering_valve, air_impact
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
# Create your views here.

def hydro_listings(request):
    metering_valve_listings = metering_valve.objects.all()
    listings = metering_valve_listings
    
    paginator = Paginator(listings, 9)
    page = request.GET.get("صفحه")
    paged_listing = paginator.get_page(page)
    listings_context = {
        "metering_valve_listings": paged_listing,
    }
    return render(request, 'pages/listings.html', listings_context)

def penu_listings(request):
    air_impact_listings = air_impact.objects.all()
    listings = air_impact_listings
    
    paginator = Paginator(listings, 9)
    page = request.GET.get("صفحه")
    paged_listing = paginator.get_page(page)
    listings_context = {
        "air_impact_listings": paged_listing,
    }
    return render(request, 'pages/listings.html', listings_context)






def hydro_listing(request,listing_id):
     metering_valve_listing = get_object_or_404(metering_valve, pk=listing_id)

     listing_context = {
         "metering_valve_listing": metering_valve_listing,
     }
     return render(request, 'pages/Hydro_portfolio-details.html', listing_context)

def penu_listing(request,listing_id):

     air_impact_listing = get_object_or_404(air_impact, pk=listing_id)
     listing_context = {
        "air_impact_listing0": air_impact_listing,
     }
     return render(request, 'pages/penu_portfolio-details.html', listing_context)


def sooon(request):

     return render(request, 'pages/soon.html', )




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

