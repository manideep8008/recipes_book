from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/')
def receipes(request):
    if request.method=='POST':
        data = request.POST
        receipe_name=data.get('receipe_name')
        receipe_desc=data.get('receipe_desc')
        receipe_image=request.FILES.get('receipe_image')
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_desc=receipe_desc,
            receipe_image=receipe_image
        )
        print(receipe_name)
        print(receipe_desc)
      
        return redirect("/recepies/")
    

    queryset=Receipe.objects.all()

    if request.GET.get('search_re'):
        queryset=queryset.filter(receipe_name__icontains=request.GET.get('search_re'))
    
    context={'receipes':queryset}
    return render(request,'receipes.html',context)


@login_required(login_url='/')
def delete_recepies(request,id):
    print(id)
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect("/recepies/")

@login_required(login_url='/')
def update_recepies(request,id):
    queryset=Receipe.objects.get(id=id)
    if request.method=="POST":
        data = request.POST
        receipe_name=data.get('receipe_name')
        receipe_desc=data.get('receipe_desc')
        receipe_image=request.FILES.get('receipe_image')
        queryset.receipe_name=receipe_name
        queryset.receipe_desc=receipe_desc
        if receipe_image:
            queryset.receipe_image=receipe_image
        queryset.save()
        return redirect("/recepies/")
    context={'receipe':queryset}
    return render(request,'update_receipe.html',context)

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request,'Invalid Username')
            return redirect('/')
        
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'Invalid username or Password')
            return redirect("/")
        else:
            login(request,user)
            return redirect("/recepies/")

    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username taken')
            return redirect('/register/')

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
            )
        user.set_password(password)
        user.save()
        messages.info(request,'Account created')
        return redirect('/register/')

    return render(request,'register.html')

def logout_page(request):
    logout(request)
    return redirect("/")
