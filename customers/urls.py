from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-profile/', views.create_customer_profile, name='create_customer_profile'),  # Correct path
    path('create-request/', views.create_request, name='create_request'),
]
