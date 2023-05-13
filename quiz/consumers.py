import imp
import json
#from time import pthread_getcpuclockid
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from . import models
import random
import ast



class gameConsumer(AsyncWebsocketConsumer):
    print('addadww321')
    async def connect(self):
        print('addadww322')
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = 'game_%s' % self.room_name

        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        print('addadww323',self.room_group_name)
        

        await self.accept()
            


    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)
        

    async def receive(self, text_data):
        print('addadww324')



        data= json.loads(text_data)
        print('Received JSON object:', data)
        username1=self.scope['user']
        self.glabaluser=username1
        self.glabaluser1=str(self.glabaluser)

        try:
            started = data['started']
        except:
            started = False
        try:
            question = data['question']
        except:
            question = False
        try:
            answer = data['answer']
        except:
            answer = False
        try:
            correctans = data['correctans']
        except:
            correctans = False
       #
        try:
            exam = data['exam']
        except:
            exam = False
        try:
            result = data['result']
        except:
            result = False
        try:
            room = data['room']
        except:
            room = False
        try:
            id = data['id']
        except:
            id = False
        try:
            players = data['players']
        except:
            players = False
        try:
            camera_correct = data['camera_correct']
        except:
            camera_correct = False
        try:
            pp = data['pp']
        except:
            pp = False

        try:
            name = data['name']
        except:
            name = False
        try:
            next = data['next']
        except:
            next = False
        try:
            end_clicked = data['end_clicked']
        except:
            end_clicked = False

        try:
            data = data['data']
        except:
            data = False
        
        
        print('fwegw22fff',camera_correct)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'word',
                'question':question,
                'answer':answer,
                'correctans':correctans,
                'exam':exam,
                'result':result,
                'room':room,
                'id':id,
                'players':players,
                'data':data,
                'camera_correct':camera_correct,
                'pp':pp,
                'name':name,
                'next':next,
                'end_clicked':end_clicked
            }
            
        )
        user = self.glabaluser1
        if result != False:
            await self.save_result(result,room,user,id,players)
        if data != False:
            await self.data(data)

    async def word(self,event):
        try:
            question = event['question']
        except:
            question = False
        try:
            answer = event['answer']
        except:
            answer = False
        try:
            correctans = event['correctans']
        except:
            correctans = False
        try:
            exam = event['exam']
        except:
            exam = False
        try:
            result = event['result']
        except:
            result = False
        try:
            room = event['room']
        except:
            room = False
        try:
            camera_correct = event['camera_correct']
        except:
            camera_correct = False
        try:
            pp = event['pp']
        except:
            pp = False
        try:
            name = event['name']
        except:
            name = False
        try:
            id = event['id']
        except:
            id = False
        try:
            next = event['next']
        except:
            next = False
        try:
            end_clicked = event['end_clicked']
        except:
            end_clicked = False
        
        print('vwbw',next)
        await self.send(text_data=json.dumps({

            'question':question,
            'answer':answer,
            'correctans':correctans,
            'exam':exam,
            'result':result,
            'room':room,
            'camera_correct':camera_correct,
            'next':next,
            'end_clicked':end_clicked
    
            
            
        }))
        if pp != False:
            await self.played_quiz(room,pp,name,id)
        print('fqegfqeg',camera_correct)
        print('addadww32',question,answer,correctans)

    @sync_to_async
    def played_quiz(self,room,players,name,id):
        print('vewngirw',id,name,room)
        from .models import played_quiz
        print('gkeqg',players)
        for i in players:
            played_quiz.objects.create(user=i,code=room,name=name,ids=id).save()
    @sync_to_async
    def save(self,room,started,end):
        startingroom.objects.create(room=room,started=started,end=end)

    @sync_to_async
    def save_result(self,result,room,glabaluser1,id,players):
        from.models import room_created
        room_created.objects.create(user=glabaluser1,table=result,room_created=room,id=id,players=players).save()


  
