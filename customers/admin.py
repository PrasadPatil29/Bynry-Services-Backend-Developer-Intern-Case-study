from django.contrib import admin
from .models import Customer, ServiceRequest

# Register models
admin.site.register(Customer)
admin.site.register(ServiceRequest)
