from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
import re
from django.contrib import auth



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
