from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-request/', views.create_request, name='create_request'),
    path('create-profile/', views.create_customer_profile, name='create_customer_profile'),
]
