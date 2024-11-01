from django.shortcuts import render, redirect, reverse

from django.http import HttpResponseRedirect

from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required

from web.models import *
from product.models import *
from .forms import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger





def login(request):
    # Sample product data; retrieve actual product from the database
    context = {
    }
    return render(request, 'web/login.html', context=context)
    

def index(request):
    products = Product.objects.all()[:8]
    services = Service.objects.all()[:3]
    categories = Category.objects.all()[:3]
    testimonials = Testimonial.objects.all()
    video = Video.objects.all()[1:]

    

    context = {
        "products": products,
        "services": services,
        "categories": categories,
        "testimonials": testimonials,
        "video": video,
        
    }
    return render(request, 'web/index.html', context=context)


def single_product_view(request, id):
    product = Product.objects.get(id=id)
    rating_as_int = int(product.rating)
    # Sample product data; retrieve actual product from the database
    context = {
        "product": product,
        "rating_as_int": rating_as_int,
    }
    return render(request, 'web/single_product.html', context=context)

def service_detail(request, id):
    service = Service.objects.get(id=id)
    return render(request, 'web/service_detail.html', {'service': service})


def services(request):
    products = Product.objects.all()
    services = Service.objects.all()
    # Sample product data; retrieve actual product from the database
    context = {
        "services": services,
    }
    return render(request, 'web/services.html', context=context)



def gallery(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', '')
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 1000)

    filter_toggle_btn = request.GET.get('filter_toggle')

    products = Product.objects.all()    
    categories = Category.objects.all()

    # Filter by search query
    if query:
        products = products.filter(name__icontains=query)
    
    # Filter by category
    if category_id:
        products = products.filter(category_id=category_id)
    
    # Filter by price range
    products = products.filter(discount__gte=min_price, discount__lte=max_price)

    # Pagination
    paginator = Paginator(products, 8 if filter_toggle_btn else 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Get the page object

    context = {
        'categories': categories,
        'query': query,
        'min_price': min_price,
        'max_price': max_price,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
        'products': page_obj,  # Update to use the paginated products
    }
    return render(request, 'web/gallery.html', context=context)




def portfolio(request):
    products = Product.objects.all()
    # Sample product data; retrieve actual product from the database
    context = {
        "products": products,
    }
    return render(request, 'web/portfolio.html', context=context)



def testimonials(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('web:testimonials')  # Redirect to the same page to show the updated list
    else:
        form = TestimonialForm()

    context = {
        'testimonials': testimonials,
        'form': form
    }

    return render(request, 'web/testimonials.html', context)




def contact(request):
    products = Product.objects.all()
    # Sample product data; retrieve actual product from the database
    context = {
        "products": products,
    }
    return render(request, 'web/contact.html', context=context)


def thanks(request):
    # Sample product data; retrieve actual product from the database
    context = {
    }
    return render(request, 'web/thank.html', context=context)


def quiz(request):
    # Sample product data; retrieve actual product from the database
    context = {
    }
    return render(request, 'web/quiz.html', context=context)



def faqs(request):
    # Sample product data; retrieve actual product from the database
    context = {
    }
    return render(request, 'web/faqs.html', context=context)


def blog(request):
    # Sample product data; retrieve actual product from the database
    context = {
    }
    return render(request, 'web/blog.html', context=context)


def product(request):
    products = Product.objects.all()

    # Sample product data; retrieve actual product from the database
    context = {
        'products': products
    }
    return render(request, 'web/produc.html', context=context)



def appointment_booking(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the appointment to the database
            return redirect('web:thanks')  # Redirect to a success page or show a success message
    else:
        form = AppointmentForm()
    
    return render(request, 'web/appointment_booking.html', {'form': form})



def careers (request):
    # Sample product data; retrieve actual product from the database
    context = {
    }
    return render(request, 'web/careers.html', context=context)


def about_us (request):
    team_members = TeamMember.objects.all()
    context = {
        'team_members': team_members
    }
    return render(request, 'web/about_us.html', context=context)



def send_message(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Send an email (you can customize this part based on your requirements)
        messages = Message.objects.create(
            name=name, 
            email=email, 
            message=message
        )
        messages.save()

        # Redirect to a thank-you page or show a success message
        return redirect('web:thanks')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def redi(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

