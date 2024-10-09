from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User

class customer(models.Model):
    LIVE = 1
    DELETE = 0
    STATUS_CHOICES = (
        (LIVE, 'Live'),
        (DELETE, 'Delete')
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.name
    

class Worksite(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Each worksite belongs to a user
    worksite_picture = models.ImageField(upload_to='worksite_pics/', null=True, blank=True)

    def __str__(self):
        return self.name

class WorksiteImage(models.Model):
    worksite = models.ForeignKey(Worksite, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='worksite_images/')
    
    def __str__(self):
        return f"Image for {self.worksite.name}"