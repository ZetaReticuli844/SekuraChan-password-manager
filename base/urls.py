from django.urls import path
from . import views
from two_factor.urls import urlpatterns as tf_urls
from django.urls import include

urlpatterns = [
    path('',views.welcome,name='welcome'),
    path('register/',views.registerPage,name='register'),
    path(r'', include(tf_urls)),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('home/<int:pk>/',views.home,name='home'),
    path('settings/<int:pk>/',views.settings,name='settings'),
    path('password_display/',views.password_display,name='password_display'),
    path('password_info/<int:pk>/',views.password_info,name='password_info'),
    path('delete_password/<int:pk>/',views.delete_password,name='delete_password'),
    path('delete_profile/<int:pk>/',views.delete_profile,name='delete_profile'),
    path('export-json/', views.export_json, name='export_json'),
    
    
]