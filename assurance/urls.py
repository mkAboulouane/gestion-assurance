
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registrationPage, name="registrationPage"),
    path('login/',views.loginPage,name="loginPage"),
    path('logout/',views.logoutPage,name="logoutPage"),
    
    path('',views.home,name="home"),  
    path('contact/',views.contact_us,name="contact_us"),
   
    path('client/',views.allclient,name="allclient"),
    path('client/<str:pk>/', views.client_id, name="client_id"),
    
    path('addclient/',views.add_Client,name="add_Client"),
    path('update/<str:pk>/',views.update_Client,name="update_Client"),
    path('delete/<str:pk>/',views.delete_Client,name="delete_Client"),
    
    ]
