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
x= ["أ","ت","ث","ج","ح","خ","د","ذ","ر","ز","س","ش","ص","ض","ط","ع","غ","ف","ق","ك","ل","م","ن","ه","و","ي"]
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

    return render(request,'endAdmin.html',{'rr':room_code,'user':req,'z':adnan.render(Context({}))})
    #return render(request,'endAdmin.html',{'user':req})
def roomentering(request):
    return render(request,'room.html')

def create(request):
    users = User.objects.all()
    room_code=random.randint(10001,99999)
    from gameadmin.models import startingroom
    x=startingroom.objects.all().filter(room=room_code).values()
    print('startingroomrrr',x)
    if str(x) == '<QuerySet []>':
        return render(request , 'create.html' ,{'users':users,'room':room_code})

    
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
        models.summeryOfLetter.objects.create(all_letter_as="['أ', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي' ]",room=room_code)
        
        return render(request,"game.html", {'username':username , 'room_code' : room_code ,'info':info , 'the_letter':the_letter ,})

    else:
        print('no is none')

        messages.error(request , 'Error, room code allready used')
        return render(request,"create.html" , {'roomcode':room_code , 'username':username ,'users':users })

    
def room_admin(request,room_code):

    info = adnan_test11.objects.filter(room=room_code)
    models.summeryOfLetter.objects.create(all_letter_as="['أ', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي' ]",room=room_code)
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
        models.summeryOfLetter.objects.create(all_letter_as="['أ', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي']",room=room_code)
        
        return render(request,"game.html", {'username':username , 'room_code' : room_code ,'info':info , 'the_letter':the_letter ,})

    



def wait(request , room_code):
    from gameadmin.models import startingroom
    x=startingroom.objects.all().filter(room=room_code).values()
    print('zzfegeg',x)
    z=False
    time=False
    admin=False
    for i in x:
        z=i['started']
        time=i['time']
        admin=i['admin']
        break

    if z != True:
        username = request.GET['username']
        return render(request , 'waiting.html' , {'room_code':room_code ,'username':username ,'time':time,'admin':admin,'x':x})
    else:
        return HttpResponse('Game already started')

def end(request , room_code):
    username = request.GET['username']
    return render(request , 'end.html',{'user':username,'room':room_code,'z':adnan.render(Context({}))})


def type(request):
    return render(request,'type.html')

def quiz(rewquest):
    return render(rewquest,'quiz.html')
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def req(rewquest):

    if rewquest.method == 'POST':
        import json
        data = (rewquest.body).decode('utf-8')
        array = json.loads(data)
        x = array[-1]
        array.pop()
        print(array )
        
        code = array[-1]
        #array.pop(-2)
        from quiz import models
        models.MyModel.objects.create(data=array,code=code).save
        print('my array tt',array)
        # process the incoming data

        models.title.objects.create(user=rewquest.user,title=x,code=code).save
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
    
def join_quiz(request):
    return render(request,'joinquiz.html')
def joinquiz(request,room_code):
    from quiz import models
    x= models.MyModel.objects.all().filter(code=room_code).values()
    array = []
    for i in x:
        e = i['data']
        array.append(e)

    


    return render(request,'gamequiz.html',{'data':array,'room_code':room_code})


def room_admin_quiz(request,room_code):
    from quiz import models
    x= models.MyModel.objects.all().filter(code=room_code).values()
    array = []
    for i in x:
        e = i['data']
        array.append(e)

    
    return render(request,'startquiz.html',{'room_code':room_code,'data':array})


def wait_quiz(request,room_code):
    username = request.GET['username']
    return render(request,'waitingquiz.html',{'room_code':room_code ,'username':username})


def camera(request,room_code):
    

    return render(request,'camera.html',{'room_code':room_code})


def room_admin_quiz_qr(request,room_code):
    from quiz import models
    x= models.MyModel.objects.all().filter(code=room_code).values()
    array = []
    for i in x:
        e = i['data']
        array.append(e)


    import io   
    import qrcode.image.svg 
    import qrcode
    context ={}
    factory = qrcode.image.svg.SvgImage
    qr_image = qrcode.make(f'https://adnan-game-animal.herokuapp.com/camera/{room_code}',image_factory=factory, box_size=10)    
    bufstore = io.BytesIO()
    qr_image.save(bufstore)    
    
    svg = bufstore.getvalue().decode() 

    return render(request,'startquiz_qr.html',{'room_code':room_code,'data':array,'svg':svg})




def room_admin_quiz_qr_end(request,room_code,id):
    from quiz import models
    valie2=models.room_created.objects.all().filter(room_created=room_code,id=id).values()
    for i in valie2:
        z2 = i['table']
        if z2!= 'False' or False:
            break
        else:
            continue

    adnan = Template(z2)


    return render(request,'end_quiz_qr.html',{'room_code':room_code,'z':adnan.render(Context({}))})



def edit(request,room_code):
    from quiz import models
    x= models.MyModel.objects.all().filter(code=room_code).values()
    array = []
    for i in x:
        e = i['data']
        array.append(e)





    return render(request,'edit.html',{'data':array})



@csrf_exempt
def req1(rewquest):

    if rewquest.method == 'POST':
        import json
        data = (rewquest.body).decode('utf-8')
        array = json.loads(data)
        x = array[-1]
        array.pop()
        print(array )
        
        code = array[-1]
        array.pop(-2)
        from quiz import models
        new = models.MyModel.objects.get(code=code)
        new.data = data
        new.save()
        new.delete()
        #models.MyModel.objects.create(data=array,code=code).save
        print('my array tt',array)
        # process the incoming data

        #models.title.objects.create(user=rewquest.user,title=x,code=code,edit=edit).save
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
    
