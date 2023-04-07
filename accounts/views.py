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
from animal import models as mbd

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
                            user = auth.authenticate(username = name , password= password)
                            auth.login(request,user)
              
                            return render(request , 'room.html')
                            
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
            return redirect('room')
        else:
            messages.error(request,'Wrong, Enter username not email!')   
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
            v = i['date']
            w.append(z)
            w.append(v)

        return render (request , 'mygames.html',{'z':w})
    else:
        return HttpResponse('please login to your account , <a href="/account/login">login</a>')

def myaccount(request,room_code):
    if request.user.is_authenticated:
        valie = mbd.room_created.objects.all().filter(user=request.user,room_created=room_code).order_by('-pk').values()
        z= valie
        for i in valie:
            z = i['table']
            if z!= 'False' or False:
                break
            else:
                continue
        print('herer er hueu is z',z)
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
    valie2 = mbd.room_created.objects.all().filter(room_created=room_code).order_by('-pk').values()
    for i in valie2:
        z2 = i['table']
        if z2!= 'False' or False:
            break
        else:
            continue
    adnan = Template(z2)

    return render (request , 'played.html',{'z':adnan.render(Context({}))})

def created(request):
    return render(request,'created.html')

def quiz(request):
    from quiz import models
    data = models.title.objects.all().filter(user=request.user).values()
    w=[]
    for i in data:
        z = i['title']
        v = i['code']
        w.append(z)
        w.append(v)

    return render(request,'quizlist.html',{'z':w})


def quiz_data(request,room_code):
    from quiz import models
    data = models.title.objects.all().filter(user=request.user,code=room_code).values()
    
    return render(request,'quiz_data.html',{'w':data})


def qrcodes(request):
    if request.user.is_authenticated:
        username = request.user.username


    import qrcode
    import numpy as np
    from PIL import Image, ImageDraw, ImageOps
    from itertools import chain

    urls = [
        "A",
        "B",
        "C",
        "D",
    ]

    # Create a list to hold the QR code images
    qr_codes = []

    # Generate QR codes for each URL
    for url in urls:
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        qr_codes.append(np.array(img.convert('RGB')))

    # Determine the size of the final image
    max_width = max([code.shape[1] for code in qr_codes])
    total_height = sum([code.shape[0] for code in qr_codes])

    # Create a new image to hold the final QR code
    final_image = Image.new("RGB", (max_width, total_height), "white")

    # Loop through the QR code images and paste them into the final image
    y_offset = 0
    for i, img in enumerate(qr_codes):
        angle = i * 90
        img = np.rot90(img, k=i)
        h, w, _ = img.shape
        x_offset = (max_width - w) // 2
        final_image.paste(Image.fromarray(img), (x_offset, y_offset))
        y_offset += h

    # Save the final image
    from django.http import HttpResponse
    from io import BytesIO

    # Your PIL Image object
    image = final_image

    # Convert the image to a byte stream
    image_byte_array = BytesIO()
    image.save(image_byte_array, format='PNG')
    image_byte_array = image_byte_array.getvalue()

    return render(request,'qrcodes.html',{'user':username,'image_byte_array':image_byte_array})