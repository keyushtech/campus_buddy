from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm

def index(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marketplace_index')
    else:
        form = ListingForm()

    listings = Listing.objects.all().order_by('-date_posted')
    return render(request, 'marketplace/index.html', {'listings': listings, 'form': form})
