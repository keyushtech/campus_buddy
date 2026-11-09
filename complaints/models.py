from django.db import models

class Complaint(models.Model):
    CATEGORY_CHOICES = [
        ('HOSTEL', 'Hostel (Maintenance / Water / Electricity)'),
        ('ACADEMIC', 'Academic Area (Classrooms / Labs / Wi-Fi)'),
        ('MESS', 'Mess / Dining Facility'),
        ('OTHER', 'General Campus Infrastructure'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Under Review'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    ]

    title = models.CharField(max_length=120)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default='HOSTEL')
    location_details = models.CharField(max_length=150, help_text="e.g., Room H301, Academic Block LH-2, Central Mess")
    description = models.TextField()
    student_contact = models.CharField(max_length=100, help_text="Roll No or Student Email")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='PENDING')
    date_filed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.category}] {self.title} - {self.status}"
class Announcement(models.Model):
    CATEGORY_CHOICES = [
        ('ACADEMIC', 'Academic Block'),
        ('HOSTEL', 'Hostel Maintenance'),
        ('SAFETY', 'Campus Safety'),
        ('GENERAL', 'General Notice'),
    ]

    title = models.CharField(max_length=150)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='GENERAL')
    content = models.TextField()
    posted_by = models.CharField(max_length=100, default='Campus Admin', help_text="e.g. Estate Office, Security Cell")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide from homepage without deleting")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.category}] {self.title}"
