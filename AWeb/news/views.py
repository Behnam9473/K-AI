from .models import News
from django.shortcuts import get_object_or_404, render

def news(request):
    # about = about_us.objects.values_list('about')

    news = News.objects.all()
    data = {
        "news": news,

    }
    return render(request,'pages/news.html',data)