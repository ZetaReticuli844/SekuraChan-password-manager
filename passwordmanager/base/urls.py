from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome,name='welcome'),
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('home/<int:pk>/',views.home,name='home'),
    path('password_display/',views.password_display,name='password_display'),
    path('password_info/<int:pk>/',views.password_info,name='password_info'),
    path('delete_password/<int:pk>/',views.delete_password,name='delete_password'),
    path('delete_profile/<int:pk>/',views.update_password,name='delete_profile'),
    
    
]