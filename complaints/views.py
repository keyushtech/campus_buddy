from django.shortcuts import render, redirect
from .models import Complaint
from .forms import ComplaintForm

def index(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complaints_index')
    else:
        form = ComplaintForm()

    complaints = Complaint.objects.all().order_by('-date_filed')
    return render(request, 'complaints/index.html', {'complaints': complaints, 'form': form})
