from django.contrib import messages
import re
from django.shortcuts import render
from .models import adnan_test11
import random
from animal import models
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.template import Template, Context
from accounts import models as md
x= ["أ","ب","ت","ث","ج","ح","خ","د","ذ","ر","ز","س","ش","ص","ض","ط","ع","غ","ف","ق","ك","ل","م","ن","ه","و","ي"]
the_letter = 'ب'
print('this is letterc from views',the_letter)

def room_end(request,room_code):
    req=request.GET['anan']
    valie = md.room_created.objects.all().filter(user=request.user,room_created=room_code).values()
    for i in valie:
        z = i['table']
        break
    global adnan
    adnan = Template(z)

    print('my is ',request.user ,z , type(z))
    return render(request,'endAdmin.html',{'rr':room_code,'user':req,'z':adnan.render(Context({}))})
    #return render(request,'endAdmin.html',{'user':req})
def roomentering(request):
    return render(request,'room.html')

def create(request):
    users = User.objects.all()

    return render(request , 'create.html' ,{'users':users})

def room(request,room_code):
    
    
    users = User.objects.all()
    mydata = models.summeryOfLetter.objects.all().values()
    t =[]
    for i in mydata:
        z = i['room']
        t.append(z)
    print("donnee")

    username = request.GET['username']
    print('room code is::' , room_code)

    try :
        info = adnan_test11.objects.filter(room=room_code)

    except:
        info=""

    mydata = models.summeryOfLetter.objects.all().values()
    t =[]
    for i in mydata:
        z = i['room']
        t.append(z)
    #print('my data is::',t)
    if str(room_code) not in t :
        print('yse is none')
        models.summeryOfLetter.objects.create(all_letter_as="['أ','ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي']",room=room_code)
        
        return render(request,"game.html", {'username':username , 'room_code' : room_code ,'info':info , 'the_letter':the_letter ,})

    else:
        print('no is none')

        messages.error(request , 'Error, room code allready used')
        return render(request,"create.html" , {'roomcode':room_code , 'username':username ,'users':users })

    
def room_admin(request,room_code):

    info = adnan_test11.objects.filter(room=room_code)
    models.summeryOfLetter.objects.create(all_letter_as="['أ','ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي']",room=room_code)
    import io   
    import qrcode.image.svg 
    import qrcode
    context ={}
    factory = qrcode.image.svg.SvgImage
    qr_image = qrcode.make(f'https://adnan-game-animal.herokuapp.com/joinqr/{room_code}',image_factory=factory, box_size=10)    
    bufstore = io.BytesIO()
    qr_image.save(bufstore)    
    
    svg = bufstore.getvalue().decode() 
    return render(request, "startroom.html", {'info': info , 'room_code':room_code ,'the_letter':the_letter,'svg':svg})

def join(request):
    return render(request,'join.html')
def joinqr(request,room_code):
    return render(request,'joinqr.html',{'room':room_code})

def joinnow(request,room_code):

    users = User.objects.all()
    mydata = models.summeryOfLetter.objects.all().values()
    t =[]
    for i in mydata:
        z = i['room']
        t.append(z)
    print("donnee")

    username = request.GET['username']
    print('room code is::' , room_code)

    try :
        info = adnan_test11.objects.filter(room=room_code)

    except:
        info=""

    mydata = models.summeryOfLetter.objects.all().values()
    t =[]
    for i in mydata:
        z = i['room']
        t.append(z)
    #print('my data is::',t)
    if True:
        print('yse is none')
        print('vies room codeis',room_code)
        models.summeryOfLetter.objects.create(all_letter_as="['أ','ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي']",room=room_code)
        
        return render(request,"game.html", {'username':username , 'room_code' : room_code ,'info':info , 'the_letter':the_letter ,})

    



def wait(request , room_code):
    from gameadmin.models import startingroom
    x=startingroom.objects.all().filter(room=room_code).values()
    print('zzfegeg',x)
    z=False
    for i in x:
        z=i['started']
        time=i['time']
        admin=i['admin']
        break

    if z != True:
        username = request.GET['username']
        return render(request , 'joinx.html' , {'room_code':room_code ,'username':username ,'time':time,'admin':admin})
    else:
        return HttpResponse('Game already started')

def end(request , room_code):
    username = request.GET['username']
    return render(request , 'end.html',{'user':username,'room':room_code,'z':adnan.render(Context({}))})