from django.shortcuts import render

# Create your views here.
# customer_service/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('service_request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_request_form.html', {'form': form})

@login_required
def service_request_list(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'service_request_list.html', {'requests': requests})

@login_required
def service_request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    return render(request, 'service_request_detail.html', {'service_request': service_request})
