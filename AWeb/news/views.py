from .models import News
from django.shortcuts import get_object_or_404, render

def news(request):
    # about = about_us.objects.values_list('about')

    news = News.objects.all()
    data = {
        "news": news,

    }
    return render(request,'pages/news.html',data)

def new(request, news_id):
     new_listing = get_object_or_404(News, pk=news_id)
     listing_context = {
        "new": new_listing,
     }
     return render(request, 'pages/news_portfolio-details.html', listing_context)