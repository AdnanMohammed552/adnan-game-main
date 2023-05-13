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
from django.shortcuts import render,redirect

x= ["أ","ت","ث","ج","ح","خ","د","ذ","ر","ز","س","ش","ص","ض","ط","ع","غ","ف","ق","ك","ل","م","ن","ه","و","ي"]
the_letter = 'ب'
print('this is letterc from views',the_letter)

from animal.models import lang
def room_end(request,room_code):
    language = 'english'

    req=request.GET['anan']
    valie = md.room_created.objects.all().filter(user=request.user,room_created=room_code).values()
    for i in valie:
        z = i['table']
        break
    global adnan
    adnan = Template(z)
    from animal.models import lang
    kfken = lang.objects.all().filter(user=request.user).values()
    for www in kfken:
        
        language =www['lang']

    return render(request,'endAdmin.html',{'rr':room_code,'user':req,'lang':language,'z':adnan.render(Context({}))})
    #return render(request,'endAdmin.html',{'user':req})
def roomentering(request):
    language = 'english'

    from quiz import models
    data = models.title.objects.all().filter(user=request.user,delete=False).values()
    from animal.models import lang
    kfken = lang.objects.all().filter(user=request.user.username).values()
    language = 'english' # assign a default value
    try:
        for www in kfken:
            language = www['lang'] # update the value if a language is found
    except:
        pass # do nothing if an exception is raised
    return render(request, 'room.html', {'w': data, 'lang': language})

def create(request):
    language = 'english'

    users = User.objects.all()
    room_code=random.randint(10001,99999)
    from gameadmin.models import startingroom
    x=startingroom.objects.all().filter(room=room_code).values()
    print('startingroomrrr',x)
    if str(x) == '<QuerySet []>':
        from animal.models import lang
        kfken = lang.objects.all().filter(user=request.user).values()
        for www in kfken:
            
            language =www['lang']

        return render(request , 'create.html' ,{'users':users,'room':room_code,'lang':language})

    
def room(request,room_code):
    language = 'english'

    
    
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
        from animal.models import lang
        kfken = lang.objects.all().filter(user=request.user).values()
        for www in kfken:
            
            language =www['lang']

        return render(request,"game.html", {'username':username , 'room_code' : room_code ,'info':info , 'the_letter':the_letter ,'lang':language})

    else:
        print('no is none')

        messages.error(request , 'Error, room code allready used')
        from animal.models import lang
        kfken = lang.objects.all().filter(user=request.user).values()
        for www in kfken:
            
            language =www['lang']
        
        return render(request,"create.html" , {'roomcode':room_code , 'username':username ,'users':users ,'lang':language})

    
def room_admin(request,room_code):
    language = 'english'


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
    from animal.models import lang
    kfken = lang.objects.all().filter(user=request.user).values()
    for www in kfken:
        
        language =www['lang']
    return render(request, "startroom.html", {'info': info , 'room_code':room_code ,'the_letter':the_letter,'svg':svg,'lang':language})

def join(request):
    language = 'english'

    from animal.models import lang
    kfken = lang.objects.all().filter(user=request.user).values()
    for www in kfken:
        
        language =www['lang']
    return render(request,'join.html',{'lang':language})
def joinqr(request,room_code):
    language = 'english'

    from animal.models import lang
    kfken = lang.objects.all().filter(user=request.user).values()
    for www in kfken:
        
        language =www['lang']
    return render(request,'joinqr.html',{'room':room_code,'lang':language})

def joinnow(request,room_code):
    language = 'english'


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
        from animal.models import lang
        kfken = lang.objects.all().filter(user=request.user).values()
        for www in kfken:
            
            language =www['lang']
        return render(request,"game.html", {'username':username , 'room_code' : room_code ,'info':info , 'the_letter':the_letter ,'lang':language})

    



def wait(request , room_code):
    language = 'english'

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
        from animal.models import lang
        kfken = lang.objects.all().filter(user=request.user).values()
        for www in kfken:
            
            language =www['lang']
        return render(request , 'waiting.html' , {'room_code':room_code ,'username':username ,'time':time,'admin':admin,'x':x,'lang':language})
    else:
        return HttpResponse('Game already started')

def end(request , room_code):
    language = 'english'

    username = request.GET['username']
    from animal.models import lang
    kfken = lang.objects.all().filter(user=request.user).values()
    for www in kfken:
        
        language =www['lang']
    return render(request , 'end.html',{'user':username,'room':room_code,'lang':language,'z':adnan.render(Context({}))})


def type(request):
    language = 'english'

    from animal.models import lang
    kfken = lang.objects.all().filter(user=request.user).values()
    for www in kfken:
        
        language =www['lang']
    return render(request,'type.html',{'lang':language})

def quiz(rewquest):
    language = 'english'

    from animal.models import lang
    kfken = lang.objects.all().filter(user=rewquest.user).values()
    for www in kfken:
        
        language =www['lang']
    from quiz import models as me
    s=me.MyModel.objects.all().values()
    arr = []
    for i in s:
        code = i['code']
        arr.append(code)
    random_number = random.randint(10000, 99999)
    while random_number in arr:
        random_number = random.randint(10000, 99999)
    if random_number not in arr:
        pass

    return render(rewquest,'quiz.html',{'lang':language,'ran_code':random_number})
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def req(rewquest):
    language = 'english'


    if rewquest.method == 'POST':
        import json
        data = (rewquest.body).decode('utf-8')
        array = json.loads(data)
        x = array[-1]
        array.pop()
        print(array )
        pri = array[-1]
        array.pop()

        code = array[-1]


        questionnumber = ((len(array))-1)/7
        questionnumber=int(questionnumber)
        print('qnum',questionnumber)

        from quiz import models
        models.MyModel.objects.create(data=array,code=code).save
        print('my array tt',array)
        # process the incoming data

        models.title.objects.create(user=rewquest.user,title=x,code=code,num=questionnumber).save

        df=models.enumeration.objects.all().filter(user=rewquest.user).values()

        print('fewgv',df)
        for v in df:
            number= v['quiz_number']
        s=models.enumeration.objects.get(user=rewquest.user)
        print('vweww',((int(number))+1))
        s.quiz_number = ((int(number))+1)
        s.save()
        models.priv.objects.create(priv=pri,code=code).save

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
    
def join_quiz(request):
    language = 'english'

    from animal.models import lang
    kfken = lang.objects.all().filter(user=request.user).values()
    for www in kfken:
        
        language =www['lang']
    return render(request,'joinquiz.html',{'lang':language})
def joinquiz(request,room_code):
    language = 'english'

    from quiz import models
    x= models.MyModel.objects.all().filter(code=room_code).values()
    array = []
    for i in x:
        e = i['data']
        array.append(e)
    from animal.models import lang
    kfken = lang.objects.all().filter(user=request.user).values()
    for www in kfken:
        
        language =www['lang']

    


    return render(request,'gamequiz.html',{'data':array,'room_code':room_code,'lang':language})


def room_admin_quiz(request,room_code):
    language = 'english'

    from quiz import models
    x= models.MyModel.objects.all().filter(code=room_code).values()
    array = []
    for i in x:
        e = i['data']
        array.append(e)

    from animal.models import lang
    kfken = lang.objects.all().filter(user=request.user).values()
    for www in kfken:
        
        language =www['lang']
    return render(request,'startquiz.html',{'room_code':room_code,'data':array,'lang':language})


def wait_quiz(request,room_code):
    language = 'english'

    from animal.models import lang
    kfken = lang.objects.all().filter(user=request.user).values()
    for www in kfken:
        
        language =www['lang']
    username = request.GET['username']
    return render(request,'waitingquiz.html',{'room_code':room_code ,'username':username,'lang':language})


def camera(request,room_code):
    language = 'english'

    from animal.models import lang
    kfken = lang.objects.all().filter(user=request.user).values()
    for www in kfken:
        
        language =www['lang']

    from quiz.models import title
    ee = title.objects.all().filter(user=request.user).values()
    user=''
    for x in ee:
        user = x['user']
    if str(request.user) == str(user):
        return render(request,'camera.html',{'room_code':room_code,'lang':language})
    else:
        return render(request,'password_enter.html',{'room_code':room_code})

def room_admin_quiz_qr(request,room_code):
    language = 'english'

    from quiz import models
    x= models.MyModel.objects.all().filter(code=room_code).values()
    array = []
    for i in x:
        e = i['data']
        array.append(e)
    b = models.title.objects.all().filter(user=request.user,code=room_code)
    p=models.priv.objects.all().filter(code=room_code).values()
    for i in p:
        private = i['private']
    if not b.exists():
        if private == True:
            return HttpResponse('<h2>Error, its not your game</h2>')
        elif private == False:
            import io   
            import qrcode.image.svg 
            import qrcode
            context ={}
            factory = qrcode.image.svg.SvgImage
            qr_image = qrcode.make(f'https://adnan-game-animal.herokuapp.com/camera/{room_code}',image_factory=factory, box_size=10)    
            bufstore = io.BytesIO()
            qr_image.save(bufstore)    
            
            svg = bufstore.getvalue().decode() 
            from animal.models import lang
            kfken = lang.objects.all().filter(user=request.user).values()
            for www in kfken:
                
                language =www['lang']

            return render(request,'startquiz_qr.html',{'room_code':room_code,'data':array,'svg':svg,'lang':language})



    else:
        import io   
        import qrcode.image.svg 
        import qrcode
        context ={}
        factory = qrcode.image.svg.SvgImage
        qr_image = qrcode.make(f'https://adnan-game-animal.herokuapp.com/camera/{room_code}',image_factory=factory, box_size=10)    
        bufstore = io.BytesIO()
        qr_image.save(bufstore)    
        
        svg = bufstore.getvalue().decode() 
        from animal.models import lang
        kfken = lang.objects.all().filter(user=request.user).values()
        for www in kfken:
            
            language =www['lang']

        return render(request,'startquiz_qr.html',{'room_code':room_code,'data':array,'svg':svg,'lang':language})




def room_admin_quiz_qr_end(request,room_code,id):
    language = 'english'

    from quiz import models
    valie2=models.room_created.objects.all().filter(room_created=room_code,id=id).values()
    for i in valie2:
        z2 = i['table']
        if z2!= 'False' or False:
            break
        else:
            continue

    adnan = Template(z2)

    from animal.models import lang
    kfken = lang.objects.all().filter(user=request.user).values()
    for www in kfken:
        
        language =www['lang']
    return render(request,'end_quiz_qr.html',{'room_code':room_code,'lang':language,'z':adnan.render(Context({}))})



def edit(request,room_code):
    language = 'english'

    from quiz import models
    x= models.MyModel.objects.all().filter(code=room_code).values()
    array = []
    for i in x:
        e = i['data']
        array.append(e)
    from animal.models import lang
    kfken = lang.objects.all().filter(user=request.user).values()
    for www in kfken:
        
        language =www['lang']

    name = models.title.objects.all().filter(code=room_code).values()
    b = models.title.objects.all().filter(user=request.user,code=room_code)
    p=models.priv.objects.all().filter(code=room_code).values()
    for i in p:
        private = i['private']
    if not b.exists():
        if private == True:
            return HttpResponse('<h2>Error, its not your game</h2>')
        elif private == False:
            for zz in name:
                e = zz['title']


            return render(request,'edit.html',{'data':array,'room_code':room_code,'lang':language,'name':e})

            
    else:
        for zz in name:
            e = zz['title']


        return render(request,'edit.html',{'data':array,'room_code':room_code,'lang':language,'name':e})



@csrf_exempt
def req1(rewquest):
    language = 'english'


    if rewquest.method == 'POST':
        import json
        data = (rewquest.body).decode('utf-8')
        print('bodyy',rewquest.body)
        array = json.loads(data)
        x = array[-1]
        array.pop()
        print(array )
        
        code = array[-1]
        from quiz import models
        new = models.MyModel.objects.get(code=code).delete()
        models.MyModel.objects.create(data=array,code=code).save
        
        #models.title.objects.create(user=rewquest.user,title=x,code=code,edit=edit).save
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


@csrf_exempt
def arabic(request):
    language = 'english'

    if request.method == 'POST':
        import json
        data = (request.body).decode('utf-8')
        print('fwef',data)

        if data == '"arabic"':
            print('ara')
            from .models import lang
            lang.objects.all().filter(user=request.user).delete()
            lang.objects.create(user=request.user,lang='arabic')

        elif data == '"english"':
            print('eng')
            from .models import lang
            lang.objects.all().filter(user=request.user).delete()

            lang.objects.create(user=request.user,lang='english')

        #models.title.objects.create(user=rewquest.user,title=x,code=code,edit=edit).save
        return JsonResponse({'success': True})
@csrf_exempt
def delete(request):
    language = 'english'

    if request.method == 'POST':
        import json
        data = (request.body).decode('utf-8')
        data1 = data.replace("'","").replace('"','')
        print('vwbwb',data1)
        from quiz import models
        s=models.MyModel.objects.get(code=data1)
        s.delete = True
        s.save()
        d=models.title.objects.get(code=data1)
        d.delete=True
        d.save()
        return JsonResponse({'success': True})


def activity(request):
    language = 'english'

    from quiz import models
    data = models.title.objects.all().filter(user=request.user).values()
    w=[]
    x = []
    for i in data:
        z = i['title']
        v = i['code']
        if i['delete'] == True:

            x.append(z)
            x.append(v)
        else:
            
            w.append(z)
            w.append(v)

    from animal.models import lang
    kfken = lang.objects.all().values()
    for www in kfken:
        
        language =www['lang']

    username = request.user.username
    from accounts.models import room_created
    valie = room_created.objects.all().filter(user=username).values()
    c=[]
    for i in valie:
        cc = i['room_created']
        ccc = i['date']
        c.append(cc)
        c.append(ccc)

    from accounts.models import played
    
    valiee = played.objects.all().filter(user=request.user).values()
    y=[]
    for i in valiee:
        yy = i['room_played']
        y.append(yy)
    
    

    return render(request,'myactivity.html',{'z':w,'lang':language,'e':x,'c':c,'y':y})



@csrf_exempt
def password(request):
    language = 'english'

    if request.method == 'POST':
        import json
        data = (request.body).decode('utf-8')
        array = json.loads(data)


        from quiz import models
        print('vwgwg',array[1],array[0])
        models.password.objects.create(code=array[1],password=array[0]).save()
        return JsonResponse('Error!')


        #models.title.objects.create(user)

@csrf_exempt
def endpointpassword(request):
    language = 'english'

    if request.method == 'POST':
        from django.template.loader import render_to_string
        import json
        data = (request.body).decode('utf-8')
        array = json.loads(data)
        code = array[0]
        passs = array[1]
        print('code is',code)
        print('passs is',passs)
        from quiz import models
        c=models.password.objects.all().filter(code=code).values()
        for i in c:
            actual_password = i['password']
        print('actual iss ',actual_password)
        if actual_password == passs:
            print('yessswer')
            return JsonResponse({'pass': True})
        else:
            print('vgwegwe224')
            return HttpResponse('Error password!!')

def camera_manage(request):
    return render(request,'camera.html')

def process_form(request,room_code):
    language = 'english'

    if request.method == 'POST':
        passs = request.POST.get('password')
        print('kewgew',passs,room_code)
        from quiz import models
        c=models.password.objects.all().filter(code=room_code).values()
        for i in c:
            actual_password = i['password']
        print('actual iss ',actual_password)
        if actual_password == passs:
            print('yessswer')
            return render(request,'camera.html',{'room_code':room_code,'lang':language})
        else:
            print('vgwegwe224')
            return HttpResponse('Error password!!')


    else:
        return HttpResponse('Error!!')
    

def view_questions(request,room_code):
    from quiz import models
    x= models.MyModel.objects.all().filter(code=room_code).values()
    array = []
    for i in x:
        e = i['data']
        array.append(e)
    b = models.title.objects.all().filter(user=request.user,code=room_code)
    p=models.priv.objects.all().filter(code=room_code).values()
    for i in p:
        private = i['private']
    if not b.exists():
        if private == True:
            return HttpResponse('<h2>Error, its not your game</h2>')
        elif private==False:
            return render(request,'view_questions.html',{'x':array})

    else:

        return render(request,'view_questions.html',{'x':array})

@csrf_exempt
def endpoint_restore(request):
    if request.method == 'POST':
        import json
        data = (request.body).decode('utf-8')
        array = json.loads(data)
        data1 = data.replace("'","").replace('"','')
        from quiz import models
        s=models.MyModel.objects.get(code=data1)
        s.delete = False
        s.save()
        d=models.title.objects.get(code=data1)
        d.delete=False
        d.save()
        return JsonResponse({'success': True})

