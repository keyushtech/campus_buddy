from django.db import models

class LostItem(models.Model):
    CATEGORY_CHOICES = [
        ('LOST', 'Lost'),
        ('FOUND', 'Found'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES, default='LOST')
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    image = models.ImageField(upload_to='lost_found_images/', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.category}] {self.title}"
