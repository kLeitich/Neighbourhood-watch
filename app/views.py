from django.shortcuts import render,redirect
from django.contrib import messages
from app.forms import UserRegistrationForm

# Create your views here.
def home(request):
    return render(request,'index.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'auth/register.html', context)

def business(request):
    return render(request,'business.html')

def add_a_business(request):
    return render(request,'add_a_business.html')