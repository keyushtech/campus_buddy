from django.contrib import admin
from .models import Complaint


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'location_details', 'student_contact', 'status', 'date_filed')

    list_filter = ('status', 'category', 'date_filed')

    search_fields = ('title', 'description', 'location_details', 'student_contact')

    list_editable = ('status',)

    ordering = ('-date_filed',)

    readonly_fields = ('date_filed',)
