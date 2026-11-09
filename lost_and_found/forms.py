from django import forms
from .models import LostItem

class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = ['title', 'description', 'category', 'location', 'contact', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g., Blue Tupperware Bottle'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Details about the item...'}),
            'category': forms.Select(),
            'location': forms.TextInput(attrs={'placeholder': 'e.g., Academic Block LH-1'}),
            'contact': forms.TextInput(attrs={'placeholder': 'e.g., Room H301 or Phone/Email'}),
        }
