from django.urls import path
from .views import create_customers, create_vehicles, create_rental, RentalListView, RentalDetailView, customer_list,vehicle_list
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('create_customers/', create_customers, name='create_customers'),
    path('rent/rental/', RentalListView.as_view(), name='rental_list'),
    path('rent/rental/<int:pk>/', RentalDetailView.as_view(), name='rental_detail'),
    path('customers/', customer_list, name='customer_list'),
    path('vehicles/', vehicle_list, name='vehicle_list'),
    path('create_vehicles/', create_vehicles, name='create_vehicles'),
    path('create_rental/', create_rental, name='create_rental'),
]
