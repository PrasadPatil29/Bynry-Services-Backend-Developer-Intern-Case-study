from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'support'

urlpatterns = [
    path('', RedirectView.as_view(url='dashboard/', permanent=True)),
    path('dashboard/', views.support_dashboard, name='dashboard'),
]
