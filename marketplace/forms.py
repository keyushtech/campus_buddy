from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'seller_contact', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g., Casio fx-991CW Calculator'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Condition, scratches, usage duration...'}),
            'price': forms.NumberInput(attrs={'placeholder': '₹ Price', 'step': '0.01'}),
            'seller_contact': forms.TextInput(attrs={'placeholder': 'Hostel Room or Phone/Email'}),
        }
