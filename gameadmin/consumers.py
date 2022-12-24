import imp
import json
#from time import pthread_getcpuclockid
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from . import models
import random
import ast
from .models import startingroom


class gameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = 'game_%s' % self.room_name

        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        

        await self.accept()
            


    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)
        

    async def receive(self, text_data):


        data= json.loads(text_data)
        try:
            started = data['started']
        except:
            started = False
        try:
            roomCode = data['room']
        except:
            roomCode = ''
        try:
            userName = data['userName']
        except:
            userName=''
        try:
            end = data['end']
        except:
            end=False
        try:
            nogame = data['nogame']
        except:
            nogame=False
        try:
            room = data['room']
        except:
            room=False
        try:
            admin = data['admin']
        except:
            admin=False
        try:
            Usere = data['Usere']
        except:
            Usere=False
        try:
            random = data['random']
        except:
            random=False
        await self.save(roomCode,started,end)
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'word',
                'started' :started,
                'userName':userName,
                'end':end,
                'nogame':nogame,
                'room':room,
                'admin':admin,
                'Usere':Usere,
                'random':random
            }
            
        )

    async def word(self,event):
        try:
            started = event['started']
        except:
            started = False
        try:
            userName = event['userName']
        except:
            userName = ''
        try:
            end = event['end']
        except:
            end= False
        try:
            nogame = event['nogame']
        except:
            nogame=False
        try:
            room = event['room']
        except:
            room=False
        try:
            admin = event['admin']
        except:
            admin=False
        try:
            Usere = event['Usere']
        except:
            Usere=False
        try:
            random = event['random']
        except:
            random=False
        print('costheta',nogame,room)
        if nogame == 'no' and room != False:
            print('fjkwlegbkwenfoe99')
            self.savve(room)

        await self.send(text_data=json.dumps({

            'started':started,
            'userName':userName,
            'end':end,
            'Usere':Usere,
            'random':random
            
            
        }))

    @sync_to_async
    def save(self,room,started,end):
        startingroom.objects.create(room=room,started=started,end=end)

    @sync_to_async
    def savve(self,room):
        from .models import room
        room.objects.create(room=room).save()