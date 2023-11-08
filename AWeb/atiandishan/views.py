from django.shortcuts import render
from .models import *


def index(request):
    # about = about_us.objects.values_list('about')
    about = about_us.objects.all()
    #parts = part.objects.all()
    cer = Testimonials.objects.all()
    over_view = overview.objects.all()
    serv = services.objects.all()

    data = {
        "about1": about,
        #"parts1": parts,
        "cer1": cer,
        "serv1": serv,
        "overview1":over_view,
    }
    return render(request,'pages/index.html',data)




