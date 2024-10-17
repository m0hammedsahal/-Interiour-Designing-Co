from django import forms
from web.models import *
from product.models import *
from web.models import *




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category  # Correct 'models' to 'model'
        fields = ['name', 'image']  # Ensure this is a list or tuple

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Category name"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'rating', 'time', 'discount', 'category']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rating (e.g., 4.5)'}),
            'time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Preparation Time'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Discount (%)'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }





class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'content', 'price', 'duration', 'image']
        
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Service name"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Short description", "rows": 3}),
            "content": forms.Textarea(attrs={"class": "form-control", "placeholder": "Detailed content", "rows": 5}),
            "price": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Service price"}),
            "duration": forms.TextInput(attrs={"class": "form-control", "placeholder": "Duration (e.g., 1 day, 2 hours)"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }



class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['product', 'name', 'image']
        widgets = {
            "product": forms.Select(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Image name"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }



class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['client_name', 'client_role', 'testimonial_text']

        widgets = {
            "client_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Client's Name"}),
            "client_role": forms.TextInput(attrs={"class": "form-control", "placeholder": "Client's Role"}),
            "testimonial_text": forms.Textarea(attrs={"class": "form-control", "placeholder": "Testimonial Message", "rows": 4}),
        }
