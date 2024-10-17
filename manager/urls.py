from django.urls import path
from manager import views

app_name = "manager"


urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("unauthorized_access/", views.unauthorized_access, name="unauthorized_access"),
    
    # design_category
    path("design_category/list/", views.design_category_list, name="design_category_list"),
    path("design_category/add/", views.design_category_add, name="design_category_add"),
    path("design_category/edit/<int:id>/", views.design_category_edit, name="design_category_edit"),
    path("design_category/delete/<int:id>/", views.design_category_delete, name="design_category_delete"),

    # design_category
    path("product/list/", views.product_list, name="product_list"),
    path("product/add/", views.product_add, name="product_add"),
    path("product/edit/<int:id>/", views.product_edit, name="product_edit"),
    path("product/delete/<int:id>/", views.product_delete, name="product_delete"),


    path('services/', views.service_list, name='service_list'),
    path('services/add/', views.service_add, name='service_add'),
    path('services/edit/<int:id>/', views.service_edit, name='service_edit'),
    path('services/delete/<int:id>/', views.service_delete, name='service_delete'),

    
    path('product-image/', views.product_image_list, name='product_image_list'),
    path('product_image/add/', views.product_image_add, name='product_image_add'),
    path('product_image/edit/<int:id>/', views.product_image_edit, name='product_image_edit'),
    path('product_image/delete/<int:id>/', views.product_image_delete, name='product_image_delete'),

    path('testimonials/', views.testimonial_list, name='testimonial_list'),
    path('testimonials/add/', views.testimonial_add, name='testimonial_add'),
    path('testimonials/edit/<int:id>/', views.testimonial_edit, name='testimonial_edit'),
    path('testimonials/delete/<int:id>/', views.testimonial_delete, name='testimonial_delete'),
]