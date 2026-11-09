from django.shortcuts import render
from .models import Listing

def index(request):
    listings = Listing.objects.all().order_by('-date_posted')
    return render(request, 'marketplace/index.html', {'listings': listings})
