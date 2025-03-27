from django.shortcuts import render, redirect
from customers.models import ServiceRequest

def support_dashboard(request):
    requests = ServiceRequest.objects.all()

    if request.method == 'POST':
        req_id = request.POST.get('req_id')
        new_status = request.POST.get('status')
        service_request = ServiceRequest.objects.get(id=req_id)
        service_request.status = new_status
        service_request.save()
        return redirect('support_dashboard')

    return render(request, 'support/dashboard.html', {'requests': requests})
