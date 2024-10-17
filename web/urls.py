from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path('single-product-view/<int:id>/', views.single_product_view, name='single_product_view'),
    path('service-detail/<int:id>/', views.service_detail, name='service_detail'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact/', views.contact, name='contact'),
    path('send_message/', views.send_message, name='send_message'),
    path('thanks/', views.thanks, name='thanks'),
    path('quiz/', views.quiz, name='quiz'),
    path('product/', views.product, name='product'),
    path('faqs/', views.faqs, name='faqs'),
    path('blog/', views.blog, name='blog'),
    path('careers/', views.careers, name='careers'),
    path('about_us/', views.about_us, name='about_us'),
    path('r/', views.redi, name='redi'),
    path('appointment_booking/', views.appointment_booking, name='appointment_booking'),


]