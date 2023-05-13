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
from animal.models import lang


language = 'english'

@csrf_protect 
def signup(request):
    language = 'english'

    
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
                            from quiz.models import enumeration
                            enumeration.objects.create(user=name,quiz_number=0)
                            user = User.objects.create_user(username = name,email=email,password=password)
                            user.save()
                            messages.info(request, 'Done', extra_tags='safe')
                            user = auth.authenticate(username = name , password= password)
                            from animal.models import lang

                            lang.objects.create(user=name,lang='english').save()

                            auth.login(request,user)
                            from animal.models import lang
                            kfken = lang.objects.all().values()
                            for www in kfken:
                                
                                language =www['lang']
              
                            return render(request , 'room.html',{'lang':language})
                            
                        else:
                            messages.error(request, 'Password not match', extra_tags='safe')
                    else:
                        messages.error(request, 'Email is incorrect', extra_tags='safe')
        
        from animal.models import lang
        kfken = lang.objects.all().values()
        for www in kfken:
            
            language =www['lang']
        return render(request , 'signup.html',{
            'name' : name ,
            'email':email,
            'password':password,
            'passwordv':passwordv,'lang':language
        })
    
    else:
        from animal.models import lang
        kfken = lang.objects.all().values()
        for www in kfken:
            
            language =www['lang']
        return render(request , 'signup.html',{'lang':language})

def login(request):
    language = 'english'

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
            from animal.models import lang
            kfken = lang.objects.all().values()
            for www in kfken:
                
                language =www['lang']
            return render(request , 'login.html' , {
                                'email' :email,
                                'password' : password,'lang':language
                            })

    else:
        from animal.models import lang
        kfken = lang.objects.all().values()
        for www in kfken:
            
            language =www['lang']
        return render(request , 'login.html' ,{'lang':language})
def logout(request):
    language = 'english'

    if request.user.is_authenticated:

        auth.logout(request)

        return redirect('room')
def mygames(request):
    language = 'english'

    if request.user.is_authenticated:
        username = request.user.username

        valie = models.room_created.objects.all().filter(user=username).values()
        w=[]
        for i in valie:
            z = i['room_created']
            v = i['date']
            w.append(z)
            w.append(v)
        from animal.models import lang
        kfken = lang.objects.all().values()
        for www in kfken:
            
            language =www['lang']
        return render (request , 'mygames.html',{'z':w,'lang':language})
    else:
        return HttpResponse('please login to your account , <a href="/account/login">login</a>')

def myaccount(request,room_code):
    language = 'english'

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
        from animal.models import lang
        kfken = lang.objects.all().values()
        for www in kfken:
            
            language =www['lang']
        return render (request , 'myaccount.html',{'y':valie,'lang':language,'z':adnan.render(Context({}))})
    else:
        return HttpResponse('please login to your account , <a href="/account/login">login</a>')
def home(request):
    language = 'english'

    from quiz import models

    data = models.title.objects.all().filter(user=request.user).values()
    from animal.models import lang
    kfken = lang.objects.all().values()
    for www in kfken:
        
        language =www['lang']

    return render (request , 'accounthome.html',{'lang':language})
def home2(request):
    language = 'english'

    from quiz import models

    data = models.title.objects.all().filter(user=request.user).values()
    from animal.models import lang
    kfken = lang.objects.all().values()
    for www in kfken:
        
        language =www['lang']
    df=models.enumeration.objects.all().filter(user=request.user).values()
    print('fewgv',df)
    for v in df:
        number= v['quiz_number']
    return render (request , 'accounthome2.html',{'lang':language,'num':number,'user':request.user})
def played(request):
    language = 'english'

    from .models import played
    
    valie = played.objects.all().filter(user=request.user).values()
    w=[]
    for i in valie:
        z = i['room_played']
        w.append(z)
    from animal.models import lang
    kfken = lang.objects.all().values()
    for www in kfken:
        
        language =www['lang']
    return render (request , 'playedas.html',{'z':w,'lang':language})
        
   

def playedacc(request,room_code):
    language = 'english'

    valie2 = mbd.room_created.objects.all().filter(room_created=room_code).order_by('-pk').values()
    for i in valie2:
        z2 = i['table']
        if z2!= 'False' or False:
            break
        else:
            continue
    adnan = Template(z2)
    from animal.models import lang
    kfken = lang.objects.all().values()
    for www in kfken:
        
        language =www['lang']

    return render (request , 'played.html',{'lang':language,'z':adnan.render(Context({}))})

def created(request):
    language = 'english'

    from animal.models import lang
    kfken = lang.objects.all().values()
    for www in kfken:
        
        language =www['lang']
    return render(request,'created.html',{'lang':language})

def quiz(request):
    language = 'english'

    from quiz import models
    data = models.title.objects.all().filter(user=request.user).values()
    w=[]
    for i in data:
        z = i['title']
        v = i['code']
        w.append(z)
        w.append(v)
    from animal.models import lang
    kfken = lang.objects.all().values()
    for www in kfken:
        
        language =www['lang']

    return render(request,'quizlist.html',{'z':w,'lang':language})


def quiz_data(request,room_code):
    language = 'english'

    from quiz import models
    data = models.title.objects.all().filter(user=request.user,code=room_code).values()
    print('gwgwe',data)
    p=models.priv.objects.all().filter(code=room_code).values()
    for i in p:
        private = i['private']
    if not data.exists():
        if private == True:
            return HttpResponse('<h2>Error, its not your game</h2>')
        elif private == False:
            from animal.models import lang
            kfken = lang.objects.all().values()
            for www in kfken:
                
                language =www['lang']
            return render(request,'quiz_data.html',{'w':data,'lang':language})
        else:
            return HttpResponse('<h2>No game with this code !!</h2>')
    else:

        from animal.models import lang
        kfken = lang.objects.all().values()
        for www in kfken:
            
            language =www['lang']
        return render(request,'quiz_data.html',{'w':data,'lang':language})


def qrcodes(request):
    language = 'english'

    if request.user.is_authenticated:
        username = request.user.username


    import qrcode
    import numpy as np
    from PIL import Image, ImageDraw, ImageOps
    from itertools import chain

    urls = [
        f"{username}/A",
        f"{username}/B",
        f"{username}/C",
        f"{username}/D",
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

    # Convert the image to a byte stream
    from io import BytesIO
    image_byte_array = BytesIO()
    final_image.save(image_byte_array, format='PNG')
    image_byte_array = image_byte_array.getvalue()

    # Encode the image as base64 string
    import base64
    encoded_string = base64.b64encode(image_byte_array).decode('utf-8')
    from animal.models import lang
    kfken = lang.objects.all().values()
    for www in kfken:
        
        language =www['lang']

    # Pass the encoded string to the template
    return render(request,'qrcodes.html',{'user':username,'encoded_string':encoded_string,'lang':language})


def quiz_data_last(request,room_code):
    language = 'english'

    from quiz import models as md
    s=md.room_created.objects.all().filter(room_created=room_code).values()
    adnan=Template(s)
    array = []
    for i in s:
        array.append(i['date'])
    #adnan.render(Context({}))
    from animal.models import lang
    kfken = lang.objects.all().values()
    for www in kfken:
        
        language =www['lang']

    b = md.title.objects.all().filter(user=request.user,code=room_code)
    p=md.priv.objects.all().filter(code=room_code).values()
    for i in p:
        private = i['private']
    if not b.exists():
        if private == True:
            return HttpResponse('<h2>Error, its not your game</h2>')
        elif private == False:
            return render(request,'last_quiz.html',{'z':s,'room_code':room_code,'lang':language})
        else:
            return HttpResponse('<h2>No game with this code !!</h2>')
    else:
        return render(request,'last_quiz.html',{'z':s,'room_code':room_code,'lang':language})


def quiz_data_last_preview(request,id,room_code):
    language = 'english'

    from quiz import models as md
    s=md.room_created.objects.all().filter(room_created=room_code,id=id).values()
    for i in s:
        z2 = i['table']
    adnan=Template(z2)
    from animal.models import lang
    kfken = lang.objects.all().values()
    for www in kfken:
        
        language =www['lang']
    b = md.title.objects.all().filter(user=request.user,code=room_code)
    p=md.priv.objects.all().filter(code=room_code).values()
    for i in p:
        private = i['private']
    if not b.exists():
        if private == True:
            return HttpResponse('<h2>Error, its not your game</h2>')
        elif private == False:
            return render(request,'last_quiz_preview.html',{'lang':language,'z':adnan.render(Context({}))})
        else:
            return HttpResponse('<h2>No game with this code !!</h2>')
    else:
        return render(request,'last_quiz_preview.html',{'lang':language,'z':adnan.render(Context({}))})
    