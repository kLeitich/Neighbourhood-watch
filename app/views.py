from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.forms import NeighborhoodAddForm, PostAddForm, UserRegistrationForm,BusinessAddForm,UpdateUserProfileForm
from app.models import Neighborhood,Profile,User,Business,Post


# Create your views here.
@login_required(login_url='login') 
def home(request):
    business=Business.objects.all()
    neighborhoods=Neighborhood.objects.all()
    posts=Post.objects.all()
    return render(request,'index.html',{'business':business,'neighborhoods':neighborhoods,'posts':posts})

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
@login_required(login_url='login') 
def business(request):
    business=Business.objects.all()
    return render(request,'business.html',{'business':business})
@login_required(login_url='login') 
def add_a_business(request):
    current_user=request.user
    # neighborhood=Neighborhood.find_neighborhood(current_user.id)
    # neighborhood=Neighborhood.objects.get(id=id)
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
@login_required(login_url='login') 
def neighborhood(request):
    neighborhoods=Neighborhood.objects.all()
    return render(request,'neighborhood.html',{'neighborhoods':neighborhoods})
@login_required(login_url='login') 
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

@login_required(login_url='login') 
def posts(request):
    posts=Post.objects.all()
    return render(request,'posts.html',{'posts':posts})

@login_required(login_url='login') 
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
    return render(request,'add_a_post.html',{'form': form})
@login_required(login_url='login') 
def profile(request):
    current_user = request.user
    user = User.objects.get(id = current_user.id)
    profile=Profile.filter_profile_by_id(user.id)
    return render(request,'profile.html',{'profile':profile})
@login_required(login_url='login') 
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    if request.method == "POST":
            form = UpdateUserProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                form.save()
                return redirect('profile') 
            else:
                return render(request,'update_profile.html',{'form':form})
    else:        
        form = UpdateUserProfileForm()
    return render(request, 'update_profile.html', {'form':form})
    