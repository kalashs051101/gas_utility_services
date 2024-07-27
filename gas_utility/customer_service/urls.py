# customer_service/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('submit_request/', views.submit_request, name='submit_request'),
    path('requests/', views.service_request_list, name='service_request_list'),
    path('requests/<int:pk>/', views.service_request_detail, name='service_request_detail'),
]

# gas_utility/urls.py

