from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Customer, ServiceRequest

# ✅ Dashboard View
@login_required
def dashboard(request):
    """Display customer dashboard with service requests."""
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        # Redirect to profile creation page if customer profile doesn't exist
        messages.warning(request, "Customer profile not found. Please create your profile.")
        return redirect('create_customer_profile')

    service_requests = ServiceRequest.objects.filter(customer=customer)

    context = {
        'customer': customer,
        'requests': service_requests
    }
    return render(request, 'customers/dashboard.html', context)


# ✅ Create Service Request View
@login_required
def create_request(request):
    """Create a new service request."""
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        messages.warning(request, "Customer profile not found. Please create your profile.")
        return redirect('create_customer_profile')

    if request.method == 'POST':
        service_type = request.POST.get('service_type')
        details = request.POST.get('details')

        ServiceRequest.objects.create(
            customer=customer,
            service_type=service_type,
            details=details
        )
        messages.success(request, "Service request created successfully!")
        return redirect('dashboard')

    return render(request, 'customers/create_request.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Customer

@login_required
def create_customer_profile(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        address = request.POST['address']
        
        customer, created = Customer.objects.get_or_create(user=request.user)
        customer.phone = phone
        customer.address = address
        customer.save()

        messages.success(request, "Profile created successfully!")
        return redirect('dashboard')

    return render(request, 'customers/create_customer_profile.html')
