from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.support_dashboard, name='support_dashboard'),
]
