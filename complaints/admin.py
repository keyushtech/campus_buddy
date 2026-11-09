from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location_details', 'status', 'date_filed')
    list_filter = ('category', 'status')
    search_fields = ('title', 'location_details', 'student_contact')
