from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
from .models import *
from .forms import SignUpForm
from django.core.paginator import Paginator
from django.db.models import Q
# from django.http import jsonResponse
from django.http import JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
# from .cart import Cart
# Create your views here.


def signupPage(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username, password = password)
            login(request, user)
            return redirect ("clinicApp:login") 
    else:
        form = SignUpForm()
    return render(request, 'clinicApp/signup.html',{'form':form})
def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect("clinicApp:home")
        else:
            messages.warning(request, "Username or Password is incorrect")
            return redirect("clinicApp:login")
    else:      
        return render(request, 'clinicApp/login1.html', {})


def logoutPage(request):
    logout(request)
    return redirect('clinicApp:home')

def home(request):
    patient = Patient.objects.all()
    return render(request, 'clinicApp/index.html', {'patient':patient})
def doctor(request):
    doctor = Doctors.objects.all()
    paginator = Paginator(doctor,9)
    page = request.GET.get('page')
    doctor = paginator.get_page(page)
    return render(request, 'clinicApp/doctors.html', {'doctor':doctor})

def doctorDetail(request,pk):
    doctorDetail = Doctors.objects.get(id=pk)
    context = {'doctorDetail':doctorDetail}
    return render(request, 'clinicApp/doctorDetail.html', context)
def pharmacy(request):
    pharmacy = Pharmacy.objects.all()
    ordering = request.GET.get('ordering', "")
    item_name = request.GET.get('itemname')
    
    if item_name != '' and item_name is not None:
        pharmacy = pharmacy.filter(name__icontains = item_name)
    if ordering:
        pharmacy = pharmacy.order_by(ordering) 
    # Paginator
    paginator = Paginator(pharmacy, 12)
    page = request.GET.get('page')
    pharmacy = paginator.get_page(page)
    return render(request, 'clinicApp/pharmacy.html', {'pharmacy':pharmacy})

def add_to_cart(request):
    user = request.user
    prod_id = request.GET.get('prod_id') 
    product = Pharmacy.objects.get(id = prod_id) 
    Order(customer = user, product = product).save()
    return redirect('clinicApp:show_cart')

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Order.objects.filter(customer=user)
        print(cart)
        total = 0
        sub_total = 0
        shipping=200
        coupon_discount=0
        grant_total = 0
        cart_product = [i for i in Order.objects.all() if i.customer == user]
        # print(cart_product)
        if cart_product:
            for i in cart_product:
                total  = (i.quantity * i.product.price)
                sub_total = sub_total + total
                grant_total = sub_total + shipping - coupon_discount
                print(total)
                
        return render(request, 'clinicApp/cart.html', {'cart':cart, 'total':total, 'sub_total':sub_total, 'grant_total':grant_total})

    else:
        return render(request, "clinicApp/empty.html", {})

def plus_cart(request):

    if request.method == "GET":
        prod_id = request.GET.get('prod_id')
        # print(prod_id)
        c = Order.objects.get (Q(product = prod_id) & Q(customer = request.user))
        c.quantity += 1
        c.save()
        total = 0
        sub_total = 0
        shipping=200
        coupon_discount=0
        cart_product = [i for i in Order.objects.all() if i.customer == request.user]
        for i in cart_product:
            total  = (i.quantity * i.product.price)
            # total = total+total
            sub_total = sub_total + total
           

        data ={
            'sub_total':sub_total,
            'quantity':c.quantity,
            'grant_total': sub_total + shipping - coupon_discount
           
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == "GET":
        prod_id = request.GET.get('prod_id')
        # print(prod_id)
        c = Order.objects.get (Q(product = prod_id) & Q(customer = request.user))
        c.quantity -= 1
        c.save()
        total = 0
        sub_total = 0
        shipping=200
        coupon_discount=0
        cart_product = [i for i in Order.objects.all() if i.customer == request.user]
        for i in cart_product:
            total  = (i.quantity * i.product.price)
            # total = total+total
            sub_total = sub_total + total

        data ={
            'sub_total':sub_total,
            'quantity':c.quantity,
            'grant_total':  sub_total + shipping - coupon_discount

        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == "GET":
        prod_id = request.GET.get('prod_id')
        # print(prod_id)
        c = Order.objects.get (Q(product = prod_id) & Q(customer = request.user))
        c.delete()
        total = 0
        sub_total = 0
        shipping=200
        coupon_discount=0
        cart_product = [i for i in Order.objects.all() if i.customer == request.user]
        for i in cart_product:
            total  = (i.quantity * i.product.price)
            # total = total+total
            sub_total = sub_total + total
        
        data ={
            'sub_total':sub_total,
            'grant_total':  sub_total + shipping - coupon_discount
        }
       
        return JsonResponse(data)
    

def checkout(request):
    return render(request, 'clinicApp/checkout.html', {})

def blog(request):
    if request.method == "POST":
        email = request.POST["email"]
        newsletter = Newsletter()
        newsletter.email = email
        newsletter.save()
    featured = Post.objects.filter(featured = True)
    latest = Post.objects.order_by('-time_stamp')[0:3]
    return render(request, 'clinicApp/blog.html', {'post':featured, 'latest':latest})


def dashboard(request):
    return render(request, 'clinicApp/adminsite.html', {})


        
   
    
