from django.db import models
from django.contrib.auth.models import User

# Customer model
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username


# Service Request model
class ServiceRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('completed', 'Completed'),
    )
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    details = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.service_type} - {self.status}"
