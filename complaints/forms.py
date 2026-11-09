from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'category', 'location_details', 'description', 'student_contact']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g., Water dispenser not cooling'}),
            'category': forms.Select(),
            'location_details': forms.TextInput(attrs={'placeholder': 'e.g., Gopad Hostel 3rd Floor / Academic LH-1'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Provide specific details...'}),
            'student_contact': forms.TextInput(attrs={'placeholder': 'Roll Number / Email / Phone'}),
        }
