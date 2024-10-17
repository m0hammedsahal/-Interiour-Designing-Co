from django.contrib import admin

from .models import *


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Service)
admin.site.register(Testimonial)

admin.site.register(Message)
admin.site.register(Appointment)