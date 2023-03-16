from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect
from faker import Faker
from .models import Customer, Rental, Vehicle, VehicleSize, VehicleType
from django.http import HttpResponse
from .forms import VehicleForm, RentalForm

def index(request):
    return render (request, 'base.html')

def create_vehicles(request, num_vehicles=10):
    fake = Faker()
    vehicle_types = VehicleType.objects.all()
    vehicle_sizes = VehicleSize.objects.all()
    print(f"vehicle_types length: {len(vehicle_types)}")
    print(f"vehicle_sizes length: {len(vehicle_sizes)}")
    vehicles_created = []
    for i in range(num_vehicles):
        vehicle_type = fake.random_element(vehicle_types)
        real_cost = fake.pydecimal(left_digits=4, right_digits=2, positive=True)
        size = fake.random_element(vehicle_sizes)
        vehicle = Vehicle(vehicle_type=vehicle_type, real_cost=real_cost, size=size)
        vehicle.save()
        vehicles_created.append(vehicle)
    context = {'num_vehicles_created': num_vehicles, 'vehicles_created': vehicles_created}
    return render(request, 'create_vehicles.html', context)

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    form = VehicleForm()
    context = {
        'vehicles': vehicles,
        'form': form
    }
    return render(request, 'vehicle_list.html', context)


def create_customers(request):
    fake = Faker()
    for i in range(10):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone_number = fake.phone_number()
        address = fake.address()
        city = fake.city()
        country = fake.country()
        customer = Customer(first_name=first_name, last_name=last_name, email=email,
                            phone_number=phone_number, address=address, city=city,
                            country=country)
        customer.save()
    return render(request, 'create_customers.html')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

class RentalDetailView(DetailView):
    model = Rental
    context_object_name = 'rental'
    template_name = 'rental_detail.html'
    

class RentalListView(ListView):
    model = Rental
    context_object_name = 'rentals'
    template_name = 'rental_list.html'
    queryset = Rental.objects.order_by('return_date', 'rental_date')

def create_rental(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_rental')
    else:
        form = RentalForm()
    context = {'form': form}
    return render(request, 'create_rental.html', context)