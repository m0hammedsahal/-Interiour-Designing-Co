from main.decorators import allow_manager

from main.functions import generate_form_errors

from main.decorators import allow_manager

from main.functions import generate_form_errors


# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.contrib.auth.decorators import login_required
from product.models import *


from web.models import *


from django.contrib.auth import logout as auth_logout

from django.contrib import messages
from .forms import *
 # Ensure only logged-in users can access the index view


# @login_required(login_url='manager:login')
# @allow_manager
def index(request):
    
    return render(request, 'manager/index.html')

def unauthorized_access(request):
    
    return render(request, 'manager/unauthorized_access.html')


def login(request):
#     if request.method == 'POST':
#         form = ManagerLoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 if user.is_manager:  # Check if the user has manager rights
#                     auth_login(request, user)  # Use Django's login function with alias
#                     return redirect('manager:index')
#                 else:
#                     messages.error(request, 'Unauthorized access.')
#                     return HttpResponse("Unauthorized", status=401)
#             else:
#                 messages.error(request, 'Invalid email or password.')
#         else:
#             messages.error(request, 'Invalid form data.') 
#     else:
#         form = ManagerLoginForm()

    return render(request, 'manager/login.html')




def logout_view(request):
    auth_logout(request)
    return redirect('manager:login')  # Redirect to the login page


def register(request):
    
    return render(request, 'manager/register.html')

# store_category

def design_category_list(request):
    instances = Category.objects.all()

    context = {
            "instances": instances,
            
    }
    return render(request, 'manager/design_category_list.html', context=context)


def design_category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:design_category_list'))
    else:
        form = CategoryForm()

    return render(request, 'manager/forms/design_category_add_form.html', {'form': form})



def design_category_edit(request, id):
    design_category = get_object_or_404(Category, id=id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=design_category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:design_category_list'))
    else:
        form = CategoryForm(instance=design_category)

    return render(request, 'manager/forms/design_category_add_form.html', {'form': form, 'is_edit': True, 'design_category': design_category})



# Delete View
def design_category_delete(request, id):
    instance = get_object_or_404(Category, id=id)
    model = instance.__class__.__name__
    if request.method == 'POST':
        instance.delete()
        return redirect('manager:testimonial_list')
    
    
    context = {
        'instance': instance,
        'model': model,
    }
    
    return render(request, 'manager/confirm_delete.html', context=context)


# Product

def product_list(request):
    instances = Product.objects.all()

    context = {
            "instances": instances,
    }
    return render(request, 'manager/product_list.html', context=context)


def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:product_list'))
    else:
        form = ProductForm()

    return render(request, 'manager/forms/product_add.html', {'form': form})



def product_edit(request, id):
    instance = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=Product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:product_list'))
    else:
        form = ProductForm(instance=Product)

    return render(request, 'manager/forms/product_add.html', {'form': form, 'is_edit': True, 'instance': instance})



# # Edit View
# def product_edit(request, id):
#     instance = get_object_or_404(Product, id=id)
#     if request.method == 'POST':
#         form = Product(request.POST, request.FILES, instance=instance)
#         if form.is_valid():
#             form.save()
#             return redirect('manager:product_list')
#     else:
#         form = ProductForm(instance=instance)
#     return render(request, 'manager/forms/product_add.html', {'form': form, 'instance': instance})


def product_delete(request, id):
    instance = get_object_or_404(Product, id=id)
    model = instance.__class__.__name__
    if request.method == 'POST':
        instance.delete()
        return redirect('manager:product_image_list')
    
    context = {
        'instance': instance,
        'model': model,
    }

    return render(request, 'manager/confirm_delete.html', context=context)




# List View service
def service_list(request):
    instances = Service.objects.all()
    return render(request, 'manager/service_list.html', {'instances': instances})

# Add View
def service_add(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manager:service_list')
    else:
        form = ServiceForm()
    return render(request, 'manager/forms/service_add.html', {'form': form})

# Edit View
def service_edit(request, id):
    instance = get_object_or_404(Service, id=id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('manager:service_list')
    else:
        form = ServiceForm(instance=instance)
    return render(request, 'manager/forms/service_add.html', {'form': form, 'instance': instance})

# Delete View
def service_delete(request, id):
    instance = get_object_or_404(Service, id=id)
    model = instance.__class__.__name__
    if request.method == 'POST':
        instance.delete()
        return redirect('manager:service_list')
    
    context = {
        'instance': instance,
        'model': model,
    }
    return render(request, 'manager/confirm_delete.html', context=context)


# photos

def product_image_list(request):
    instances = ProductImage.objects.all()
    return render(request, 'manager/product_image_list.html', {'instances': instances})


def product_image_add(request):
    if request.method == 'POST':
        form = ProductImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manager:product_image_list')
    else:
        form = ProductImageForm()
    return render(request, 'manager/forms/product_image_add.html', {'form': form})

def product_image_edit(request, id):
    instance = get_object_or_404(ProductImage, id=id)
    if request.method == 'POST':
        form = ProductImageForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('manager:product_image_list')
    else:
        form = ProductImageForm(instance=instance)
    return render(request, 'manager/product_image_list.html', {'form': form, 'instance': instance})

def product_image_delete(request, id):
    instance = get_object_or_404(ProductImage, id=id)
    model = instance.__class__.__name__
    if request.method == 'POST':
        instance.delete()
        return redirect('manager:product_image_list')
    
    
    context = {
        'instance': instance,
        'model': model,
    }
    return render(request, 'manager/confirm_delete.html', context=context)




# tersjhdmf

# List View
def testimonial_list(request):
    instances = Testimonial.objects.all()
    return render(request, 'manager/testimonial_list.html', {'instances': instances})

# Add View
def testimonial_add(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager:testimonial_list')
    else:
        form = TestimonialForm()
    return render(request, 'manager/forms/testimonial_add.html', {'form': form})

# Edit View
def testimonial_edit(request, id):
    instance = get_object_or_404(Testimonial, id=id)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('manager:testimonial_list')
    else:
        form = TestimonialForm(instance=instance)
    return render(request, 'manager/forms/testimonial_add.html', {'form': form, 'instance': instance})

# Delete View
def testimonial_delete(request, id):
    instance = get_object_or_404(Testimonial, id=id)
    model = instance.__class__.__name__
    if request.method == 'POST':
        instance.delete()
        return redirect('manager:testimonial_list')
    
    
    context = {
        'instance': instance,
        'model': model,
    }
    
    return render(request, 'manager/confirm_delete.html', context=context)
