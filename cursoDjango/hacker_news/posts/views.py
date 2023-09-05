from django.shortcuts import render
from .models import Posts

# Create your views here.
def home(request):
    handler = {
        "news": Posts.objects.all()
    }
    return render(request, 'website/home.html', handler)