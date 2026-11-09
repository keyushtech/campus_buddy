from django.shortcuts import render, redirect
from .models import LostItem
from .forms import LostItemForm

def index(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lost_and_found_index')
    else:
        form = LostItemForm()

    items = LostItem.objects.all().order_by('-date_posted')
    return render(request, 'lost_and_found/index.html', {'items': items, 'form': form})
