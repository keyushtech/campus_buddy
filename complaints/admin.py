from django.contrib import admin
from .models import Complaint,Announcement


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'location_details', 'student_contact', 'status', 'date_filed')

    list_filter = ('status', 'category', 'date_filed')

    search_fields = ('title', 'description', 'location_details', 'student_contact')

    list_editable = ('status',)

    ordering = ('-date_filed',)

    readonly_fields = ('date_filed',)

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'posted_by', 'is_active', 'date_posted')
    list_filter = ('category', 'is_active', 'date_posted')
    list_editable = ('is_active',)
    search_fields = ('title', 'content', 'posted_by')
