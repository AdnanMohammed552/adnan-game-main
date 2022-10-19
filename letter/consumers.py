import imp
import json
#from time import pthread_getcpuclockid
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from . import models
import random
import ast

class gameConsumer(AsyncWebsocketConsumer):
    import imp
import json
from tkinter.messagebox import NO
#from time import pthread_getcpuclockid
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from animal import models   
import random
import ast

class gameConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = 'game_%s' % self.room_name

        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        

        await self.accept()
            


    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)
        

    async def receive(self, text_data):
        print('its consemers')
        data= json.loads(text_data)
        try:
            wantletter=data['wantletter']
        except:
            wantletter=''
        try:
            wantletter1=data['wantletter1']
        except:
            wantletter1=''
        try:
            RoomCode=data['RoomCode']
        except:
            RoomCode=''
            
        await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type':'word',
                    'wantletter':wantletter,
                    'wantletter1':wantletter1,
                    'RoomCode':RoomCode

                
                }
        )
    async def word(self,event):
        try:
            wantletter=event['wantletter']
        except:
            wantletter=''
        try:
            wantletter1=event['wantletter1']
        except:
            wantletter1=''
        try:
            RoomCode=event['RoomCode']
        except:
            RoomCode=''

        if wantletter== 'value' and wantletter1=='value':
            print('consumer room cide is',RoomCode)
            e = await self.des(RoomCode)
            print('e is ::' , e)
            e = str(e)
            t = e.strip("][")
            p =t.replace("'" , '')
            r=p.split(', ')
            #print('r is ::' , r)
            the_letter_choosen = random.choice(r)
            #print('the choosen letter is :' , the_letter_choosen)
            # print('the letter chooses is ::' , the_letter_choosen)
            r.remove(the_letter_choosen)
            print('gf',the_letter_choosen)
            print('last string is ::' , r)
            await self.save(r,RoomCode)
            await self.send(text_data=json.dumps({
                'choosens':the_letter_choosen,
                'block':False

            }))
    @sync_to_async
    def des(self,RoomCode):
        #print(models.summeryOfLetter.objects.all.order_by('-time').first())
        mydata = models.summeryOfLetter.objects.all().filter(room=RoomCode).order_by('-pk').values()
        for i in mydata:
            print('consumer i is:',i)
            #global z
            z = i['all_letter_as']            
            break
        #print('z is ::' , z)
        return z
    @sync_to_async
    def save(self ,x,RoomCode ):
        x =models.summeryOfLetter(all_letter_as=x,room=RoomCode)
        x.save()