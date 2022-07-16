from django.urls import path, include
app_name = 'clinicApp'
from .import views
urlpatterns = [
    path('', views.home, name="home"),
    path('signup/',views.signupPage, name="signup"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('doctor/', views.doctor, name="doctor"),
    path('doctor/doctordetail/<int:pk>', views.doctorDetail, name="doctorDetail"),
    path('pharmacy/', views.pharmacy, name="pharmacy"),
    path('carts/', views.add_to_cart, name="cart"),
    path('showcart/',views.show_cart, name="show_cart"),
    path('pluscart/', views.plus_cart, name="pluscart"),
    path('minuscart/',views.minus_cart, name="minuscart"),
    path('removecart',views.remove_cart, name="removecart"),
    path('checkout/', views.checkout, name="checkout"),
    path('blog/', views.blog, name='blog'),
    path('dashboard/', views.dashboard, name="dashboard"),
    
]
