from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('installation', 'Installation'),
        ('repair', 'Repair'),
        ('maintenance', 'Maintenance'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    details = models.TextField()
    attachment = models.FileField(upload_to='media/', blank=True, null=True)
    status = models.CharField(max_length=20, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.request_type}'
