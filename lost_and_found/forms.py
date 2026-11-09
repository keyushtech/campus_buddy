from django import forms
from .models import LostItem

class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = ['title', 'description', 'category', 'location', 'contact']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., Blue Tupperware Bottle'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': 'Details about the item...'}),
            'category': forms.Select(attrs={'class': 'form-input'}),
            'location': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., Academic Block LH-1'}),
            'contact': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., Room H301 or Phone/Email'}),
        }
