from statistics import mode
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
import re
from django.contrib import auth
from .import models
from django.template import Template, Context
from django.views.decorators.csrf import csrf_protect

@csrf_protect 
def signup(request):
    if request.POST and 'signupbtn' in request.POST:
        name = None
        email = None
        password = None
        passwordv = None
        if 'name' in request.POST :
            name = request.POST['name']
        else:
            messages.error(request, 'Error in name', extra_tags='safe')
        if 'email' in request.POST :
            email = request.POST['email']
        else:
            messages.error(request, 'Error in email', extra_tags='safe')
        if 'password' in request.POST :
            password = request.POST['password']
        else:
            messages.error(request, 'Error in password', extra_tags='safe')
        if 'passwordv' in request.POST :
            passwordv = request.POST['passwordv']
        else:
            messages.error(request, 'Error in password', extra_tags='safe')

        if name and email and password and passwordv:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists', extra_tags='safe')
            else:
                if User.objects.filter(username=name).exists():
                    messages.error(request, 'Username already exists', extra_tags='safe')
                else:
                    patt = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
                    if re.match(patt , email):
                        if password == passwordv:
                            user = User.objects.create_user(username = name,email=email,password=password)
                            user.save()
                            messages.info(request, 'Done', extra_tags='safe')
                            return redirect('/account/login' , kwargs={'email':email,'password':password})
                        else:
                            messages.error(request, 'Password not match', extra_tags='safe')
                    else:
                        messages.error(request, 'Email is incorrect', extra_tags='safe')
        
              
        return render(request , 'signup.html',{
            'name' : name ,
            'email':email,
            'password':password,
            'passwordv':passwordv
        })
    
    else:
        return render(request , 'signup.html')

def login(request):
    if request.POST and 'loginbtn' in request.POST:
        email = request.POST['email']
        password= request.POST['password']
        user = auth.authenticate(username = email , password= password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Done login')  
            return render(request , 'login.html' , {
                                'email' :email,
                                'password' : password
                            })
        else:
            messages.error(request,'Wrong3')   
            return render(request , 'login.html' , {
                                'email' :email,
                                'password' : password
                            })

    else:
        return render(request , 'login.html' )
def logout(request):
    if request.user.is_authenticated:

        auth.logout(request)

        return redirect('room')
def mygames(request):
    if request.user.is_authenticated:
        username = request.user.username

        valie = models.room_created.objects.all().filter(user=username).values()
        w=[]
        for i in valie:
            z = i['room_created']
            w.append(z)

        return render (request , 'mygames.html',{'z':w})
    else:
        return HttpResponse('please login to your account , <a href="/account/login">login</a>')
def myaccount(request,room_code):
    if request.user.is_authenticated:
        from animal import models as mbd
        valie = mbd.room_created.objects.all().filter(user=request.user,room_created=room_code).order_by('-pk').values()
        for i in valie:
            z = i['table']
            break
        adnan = Template(z)

        print('my is ',request.user ,z , type(z))
        return render (request , 'myaccount.html',{'y':valie,'z':adnan.render(Context({}))})
    else:
        return HttpResponse('please login to your account , <a href="/account/login">login</a>')
def home(request):
    return render (request , 'accounthome.html')

def played(request):
    from .models import played
    valie = played.objects.all().filter(user=request.user).values()
    w=[]
    for i in valie:
        z = i['room_played']
        w.append(z)
    return render (request , 'playedas.html',{'z':w})
        
   

def playedacc(request,room_code):
    valie2 = models.room_created.objects.all().filter(room_created=room_code).order_by('-pk').values()
    for i in valie2:
        z2 = i['table']
        break
    adnan = Template(z2)

    return render (request , 'played.html',{'z':adnan.render(Context({}))})
    