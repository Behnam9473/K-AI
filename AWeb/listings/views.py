from django.shortcuts import get_object_or_404, render
from .models import part
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
# Create your views here.

def listings(request):
    listings = part.objects.all()
    paginator = Paginator(listings, 9)
    page = request.GET.get("صفحه")
    paged_listing = paginator.get_page(page)
    listings_context = {
        "serv1": paged_listing,
    }
    return render(request, 'pages/listings.html', listings_context)

def listing(request,listing_id):

    listing = get_object_or_404(part, pk=listing_id)
    listing_context = {
        "listing": listing,
    }
    return render(request, 'pages/portfolio-details.html', listing_context)

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