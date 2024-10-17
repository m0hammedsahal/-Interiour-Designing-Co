from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator




class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categorys')

    class Meta:
        db_table = 'product_category'
        verbose_name = ('category')
        verbose_name_plural = ('categorys')
        ordering = ['-id']

    def __str__(self):
        return self.name
    




class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    rating = models.FloatField()
    time = models.CharField(max_length=255)
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Enter a discount value between 0 and 100"
    )
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_product'
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['-id']

    def __str__(self):
        return self.name




class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='restorants')

    class Meta:
        db_table = 'product_product_image'

    def __str__(self):
        return f"{self.product.name} - Image({self.name}) in {self.product.category} "




class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()  # New field for additional content
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()
    image = models.ImageField(upload_to='services')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'service'
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['-created_at']

    def __str__(self):
        return self.name



class Testimonial(models.Model):
    client_name = models.CharField(max_length=255)  # e.g., "Jane Doe"
    client_role = models.CharField(max_length=255)  # e.g., "Homeowner"
    testimonial_text = models.TextField()  # e.g., the testimonial message
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the date when created

    class Meta:
        db_table = 'testimonial'
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['-created_at']

    def __str__(self):
        return f'Testimonial from {self.client_name}'



class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255) 
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  

    class Meta:
        db_table = 'Message'
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['-created_at']

    def __str__(self):
        return self.message


class Appointment(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    preferred_date = models.DateField()
    preferred_time = models.CharField(max_length=10)  # Store time as a string (e.g., 'morning')
    message = models.TextField(blank=True, null=True)  # Optional message

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.preferred_date} {self.preferred_time}"
    

