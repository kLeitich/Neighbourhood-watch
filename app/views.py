from django.shortcuts import render,redirect
from django.contrib import messages
from app.forms import NeighborhoodAddForm, PostAddForm, UserRegistrationForm,BusinessAddForm


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
    current_user=request.user
    if request.method == 'POST':
        form = BusinessAddForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.save()
            

            messages.success(request, f'Your business has been added.')    
            return redirect('business')
    else:
        form = BusinessAddForm()
    return render(request,'add_a_business.html',{'form': form})

def neighborhood(request):
    return render(request,'neighborhood.html')

def add_a_neighborhood(request):
    current_user=request.user
    if request.method == 'POST':
        form = NeighborhoodAddForm(request.POST, request.FILES)
        if form.is_valid():
            neighborhood = form.save(commit=False)
            neighborhood.admin = current_user
            neighborhood.save()
            

            messages.success(request, f'Your neighborhood has been added.')    
            return redirect('neighborhood')
    else:
        form = NeighborhoodAddForm()
    return render(request,'addaneighborhood.html',{'form': form})


def posts(request):
    return render(request,'posts.html')


def add_a_post(request):
    current_user=request.user
    if request.method == 'POST':
        form = PostAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            

            messages.success(request, f'Your post has been added.')    
            return redirect('posts')
        else:
            form=PostAddForm()
    return render(request,'add_a_post.html')