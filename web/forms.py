from django import forms
from product.models import *

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['client_name', 'client_role', 'testimonial_text']



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['full_name', 'email', 'phone', 'preferred_date', 'preferred_time', 'message']
        
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter your full name', "class": "input-animate mt-2 block w-full p-3 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address', "class":"input-animate mt-2 block w-full p-3 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" }),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number', "class": "input-animate mt-2 block w-full p-3 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"}),
            'preferred_date': forms.DateInput(attrs={'type': 'date', "class": "input-animate mt-2 block w-full p-3 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"}),
            'preferred_time': forms.Select(attrs={"class": "input-animate mt-2 block w-full p-3 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"}, choices=[
                ('', 'Select a time slot'),
                ('morning', 'Morning (9:00 AM - 12:00 PM)'),
                ('afternoon', 'Afternoon (12:00 PM - 3:00 PM)'),
                ('evening', 'Evening (3:00 PM - 6:00 PM)'),
            ]),
            'message': forms.Textarea(attrs={'placeholder': 'Let us know if you have any specific requests...', "class": "input-animate mt-2 block w-full p-3 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"}),
        }
