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

    # Get fresh data from database
    requests = ServiceRequest.objects.filter(customer=customer).select_related('customer')
    
    # Count by status
    pending_count = requests.filter(status='pending').count()
    resolved_count = requests.filter(status__in=['resolved', 'completed']).count()
    in_progress_count = requests.filter(status='in_progress').count()
    total_count = requests.count()

    context = {
        'customer': customer,
        'requests': requests.order_by('-updated_at'),  # Show most recently updated first
        'total_count': total_count,
        'pending_count': pending_count,
        'resolved_count': resolved_count,
        'in_progress_count': in_progress_count,
    }
    return render(request, 'dashboard.html', context)


# ✅ Create Service Request View
@login_required
def create_request(request):
    """Create a new service request."""
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        messages.warning(request, "Customer profile not found. Please create your profile.")
        return redirect('customers:create_customer_profile')

    if request.method == 'POST':
        service_type = request.POST.get('service_type')
        details = request.POST.get('details')

        ServiceRequest.objects.create(
            customer=customer,
            service_type=service_type,
            details=details
        )
        messages.success(request, "Service request created successfully!")
        return redirect('customers:dashboard')

    return render(request, 'create_request.html')


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

    return render(request, 'create_customer_profile.html')
