from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Patient)
admin.site.register(Doctors)
admin.site.register(Pharmacy)
admin.site.register(Order)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Newsletter)
admin.site.register(DoctorCategories)