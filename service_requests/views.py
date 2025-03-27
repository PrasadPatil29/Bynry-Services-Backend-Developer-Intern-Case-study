from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from django.contrib.auth import authenticate, login, logout


@login_required
def create_request(request):
    if request.method == 'POST':
        service_type = request.POST['service_type']
        details = request.POST['details']
        file = request.FILES.get('file')

        ServiceRequest.objects.create(
            user=request.user,
            service_type=service_type,
            details=details,
            file=file
        )
        return redirect('view_requests')

    return render(request, 'create_request.html')
@login_required
def view_requests(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'view_requests.html', {'requests': requests})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('view_requests')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')