from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DeliveryHistory
from django.utils import timezone


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")


@login_required(login_url='login')
def homepage(request):
    return render(request, "homepage.html")


@login_required(login_url='login')
def fuel_view(request):
    return render(request, "fuel.html")


@login_required(login_url='login')
def history_view(request):
    return render(request, "history.html")


@login_required(login_url='login')
def product_view(request):
    return render(request, "product.html")


@login_required(login_url='login')
def sales_view(request):
    return render(request, "sales.html")


def logout_view(request):
    logout(request)
    return redirect("login")


def webpage6(request):
    if request.method == 'POST':
        try:
            # Get form data
            petroleum_name = request.POST.get('petroleum_name')
            supplier = request.POST.get('supplier')
            delivery_code = request.POST.get('delivery_code')
            date_deliver = request.POST.get('date_deliver')
            total_volume = request.POST.get('total_volume')
            total_price = request.POST.get('total_price')

            # Create new delivery record
            delivery = DeliveryHistory(
                petroleum_name=petroleum_name,
                supplier=supplier,
                delivery_code=delivery_code,
                date_deliver=date_deliver,
                total_volume=total_volume,
                total_price=total_price
            )
            delivery.save()
            messages.success(request, 'Delivery record saved successfully!')
            return redirect('webpage6')
        except Exception as e:
            messages.error(request, f'Error saving delivery record: {str(e)}')
            return redirect('webpage6')

    # Get all delivery records
    deliveries = DeliveryHistory.objects.all().order_by('-date_deliver')
    return render(request, 'history.html', {'deliveries': deliveries})


def delete_delivery(request, delivery_id):
    if request.method == 'POST':
        delivery = get_object_or_404(DeliveryHistory, id=delivery_id)
        delivery.delete()
        messages.success(request, 'Delivery record deleted successfully!')
    return redirect('webpage6')
