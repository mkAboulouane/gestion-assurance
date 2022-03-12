from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Client
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .form import ClientForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def loginPage(request):   
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
      
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
      
        try:
           user = User.objects.get(username=username)
        except:
           messages.error(request,'user n''existe pas') 
        
        user = authenticate(request, username=username,password=password)  
        if user is not None:
            login(request,user)
            return redirect('home')
        else: 
            messages.error(request,'user or password not correct') 
    context={'page':page}
    return render(request,'login.html',context)

def registrationPage(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == 'POST':        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'ereur lors la Creation d''Utilisateur ')
            
    return render(request, 'login.html', {'form': form})


@login_required(login_url='loginPage')
def logoutPage(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request,'home.html')

def contact_us(request):
    return render(request,'contact_us.html')

@login_required(login_url='loginPage')
def allclient(request):
    clients = Client.objects.all()  
    context = {'clients':clients}
    return render(request,'client.html', context)
 
@login_required(login_url='loginPage') 
def client_id(request,pk):    
    clients = Client.objects.get(id=pk)
    context = {'clients':clients}
    return render(request,'clientid.html', context)

@login_required(login_url='loginPage')
def add_Client(request):
    form = ClientForm()  
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.host = request.user
            form.save()
            return redirect('allclient')
    context ={'form': form}
    return render(request,'add_client_form.html',context)

@login_required(login_url='loginPage')
def update_Client(request,pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    
    if request.method == 'POST':
        form = ClientForm(request.POST,instance=client) 
        if form.is_valid():
            form.save()
            return redirect('/client/')    
    context = {'form': form, 'obj':client }
    return render(request,'update_client_form.html',context)

@login_required(login_url='loginPage')
def delete_Client(request,pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('allclient')
    return render(request,'delete.html',{'obj':client})