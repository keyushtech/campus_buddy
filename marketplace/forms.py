from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'seller_contact']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g., Engineering Mathematics Textbook'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Condition, edition, etc.'}),
            'price': forms.NumberInput(attrs={'placeholder': '₹ Price', 'step': '0.01'}),
            'seller_contact': forms.TextInput(attrs={'placeholder': 'Hostel Room or Phone/Email'}),
        }
