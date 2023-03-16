from django import forms
from .models import Vehicle, Customer, Rental

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'country')

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_type', 'real_cost', 'size']

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['rental_date', 'return_date', 'customer', 'vehicle']



