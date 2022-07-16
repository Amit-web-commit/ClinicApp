from django.db import models
from django.urls import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete = models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.EmailField()


class Patient(models.Model):
    patientImage = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=20)
    detail = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Patients"
        verbose_name_plural = "Patients"
    def __str__(self):
        return self.name

class DoctorCategories(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "DoctorCategories"
        verbose_name_plural = "DoctorCategories"

    def __str__(self):
        return self.name

class Doctors(models.Model):
    doctorImage = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=20)
    speciality = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    Education = models.CharField(max_length=400)
    # categories = models.ForeignKey(DoctorCategories, on_delete= models.CASCADE, null=True, blank=True, default=2)

    class Meta:
        verbose_name = "Doctors"
        verbose_name_plural = "Doctors"

    def __str__(self):
        return self.name
    
CATEGORY_CHOICES = (
    ('Covid Essentials', 'Covid Essentials'),
    ('Ayurvedic', 'Ayurvedic'),
    ('Homeopathy', 'Homeopathy'),
    ('Fitness', 'Fitness'),
    ('Surgical', 'Surgical'),
    ('Sexual Wellness', 'Sexual Wellness')
)
class Pharmacy(models.Model):
    productImage = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.CharField(max_length=50, choices= CATEGORY_CHOICES)
    
    class Meta:
        verbose_name = "Pharmacy"
        verbose_name_plural = "Pharmachies"
        ordering = ('name',)

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    customer =  models.ForeignKey(User,on_delete = models.CASCADE )
    product = models.ForeignKey(Pharmacy, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.id)


User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

class Newsletter(models.Model):
    email = models.EmailField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Newsletters"
        verbose_name_plural = "Newsletters"

    def __str__(self):
        return self.email
