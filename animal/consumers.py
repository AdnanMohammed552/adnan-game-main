import json
#from time import pthread_getcpuclockid
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from . import models
from letter import models as m
import random
from accounts import models as models2

class gameConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = 'game_%s' % self.room_name
        self.user= self.scope['user']
        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        

        await self.accept()
            


    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)
        

    async def receive(self, text_data):
        print('its consemers')
        data= json.loads(text_data)
        username1=self.scope['user']
        self.glabaluser=username1
        print('https',username1)
        if(username1.is_authenticated): 
            username_str = username1.username
            print('www.',type(username_str))

        try:
            gnoun = data['gnoun']
        except:
            gnoun = ''    
        try:
            noun = data['Noun']
        except:
            noun = ''    
        try:
            animal = data['animal']
        except:
            animal = ''    
        try:
            plants = data['plants']
        except:
            plants = ''    
        try:
            countries = data['countries']
        except:
            countries = ''    
        try:
            inanimate = data['inanimate']
        except:
            inanimate = ''    
        try:
            sum = data['sum']
        except:
            sum = ''    
        try:
            username = data['UserName']
        except:
            username = ''    
        try:
            RoomCode = data['RoomCode']
        except:
            RoomCode = ''    
        try:
            the_letter= data['the_letter']
        except:
            the_letter= ''    
        try:
            end = data['end']
        except:
            end = False   
        try:
            pret =data['pret']
        except:
            pret= False
        try:
            current_letter_this = data['current_letter_this']
        except:
            current_letter_this= None
        try:
            preg=data['preg']
        except:
            preg=False
        try:
            current_letter_this1=data['current_letter_this1']
        except:
            current_letter_this1=None
        try:
            array50=data['array50']
        except:
            array50=None
        try:
            players=data['players']
        except:
            players=None
        try:
            admin_letter=data['admin_letter']
        except:
            admin_letter=None
        try:
            main_row=data['main_row']
        except:
            main_row=True
        try:
            noun_result=data['noun_result']
        except:
            noun_result=None
        try:
            gnoun_result=data['gnoun_result']
        except:
            gnoun_result=None
        try:
            animal_result=data['animal_result']
        except:
            animal_result=None
        try:
            plants_result=data['plants_result']
        except:
            plants_result=None
        try:
            countries_result=data['countries_result']
        except:
            countries_result=None
        try:
            inanimate_result=data['inanimate_result']
        except:
            inanimate_result=None
        try:
            sum=data['sum']
        except:
            sum=None
        try:
            review=data['review']
        except:
            review=False
        try:
            oneortwo=data['oneortwo']
        except:
            oneortwo=False
        try:
            error=data['error']
        except:
            error=False
        try:
            players_game=data['players_game']
        except:
            players_game=False
        try:
            noun_review=data['noun_review']
        except:
            noun_review=False
        try:
            result=data['result']
        except:
            result=False
        try:
            wantletter=data['wantletter']
        except:
            wantletter=False
        try:
            wantletter1=data['wantletter1']
        except:
            wantletter1=False
        try:
            last=data['last']
        except:
            last=False
        try:
            private=data['private']
        except:
            private=False
        try:
            block=data['block']
        except:
            block=False
        try:
            letterconsumer=data['letterconsumer']
        except:
            letterconsumer=False
        try:
            ready=data['ready']
        except:
            ready=False
        try:
            kick=data['kick']
        except:
            kick=False
        try:
            user=data['user']
        except:
            user=""
        try:
            star=data['star']
        except:
            star=False
        try:
            alltables=data['alltables']
        except:
            alltables=False
        try:
            adnan=data['adnan']
        except:
            adnan=False
        try:
            alltables2=data['alltables2']
        except:
            alltables2=False   
        try:
            disabled=data['disabled']
        except:
            disabled=False 
        try:
            player_this=data['player_this']
        except:
            player_this=False 
        try:
            room_this=data['room_this']
        except:
            room_this=False 
        try:
            alltables2=data['alltables2']
        except:
            alltables2=False 

        try:
            kickme=data['kickme']
        except:
            kickme=False 
        try:
            userf=data['userf']
        except:
            userf=False 
        print(inanimate )
        self.glabaluser1=str(self.glabaluser)
        await self.save_info(noun,gnoun,animal,plants,countries,inanimate,username,the_letter,RoomCode)
        if room_this != False:
            print('romeinoe',room_this,player_this)
            await self.thisis(player_this=player_this,room_this=room_this)
        try:
            data['type']
            
        except:
            
            pass
        await self.alltabels2(self.glabaluser1,RoomCode, alltables2)
        if players != None:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type':'word',
                    'RoomCode':RoomCode,
                    'players':players                   
                }
                
            )
        if players == None:
            await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        
                        'type':'word',
                        'players':None,

                        'pret':pret,
                        'Noun':noun,
                        'gnoun':gnoun,
                        'animal':animal,
                        'plants':plants,
                        'countries':countries,
                        'inanimate':inanimate,
                        'UserName':username,
                        'preg':preg,
                        'RoomCode':RoomCode,
                        'end':end,
                        'current_letter_this':current_letter_this,
                        'current_letter_this1':current_letter_this1,
                        'array50':array50,
                        'admin_letter':admin_letter,
                        'main_row':main_row,
                        'noun_result':noun_result,
                        'gnoun_result':gnoun_result,
                        'animal_result':animal_result,
                        'plants_result':plants_result,
                        'countries_result':countries_result,
                        'inanimate_result':inanimate_result,
                        'sum':sum,
                        'review':review,
                        'oneortwo':oneortwo,
                        'error':error,
                        'players_game':players_game,
                        'noun_review':noun_review,
                        'result':result,
                        'wantletter':wantletter,
                        'wantletter1':wantletter1,
                        'last':last,
                        'private':private,
                        'block':block,
                        'letterconsumer':letterconsumer,
                        'ready':ready,
                        'kick':kick,
                        'user':user,
                        'star':star,
                        'alltables':alltables,
                        'adnan':adnan,
                        'alltables2':alltables2,
                        'disabled':disabled,
                        'kickme':kickme,
                        'userf':userf

                    
                    }
                    
                )
   
    async def word(self,event):
        try:
            x = event['players'] 
        except:
            x= None
        print('fegbo is',x)
        if x!= None:
            RoomCode = event['RoomCode']
            print('rooomis',RoomCode)
            players=event['players']
            await self.player_save(RoomCode,players)
            player_fetched=await self.player(RoomCode)
            print('player_fetched is',player_fetched)
            await self.send(text_data=json.dumps({
                'playersfetch':player_fetched
            }))
        else:
            try:
                noun = event['Noun']
            except:
                noun =''
            try:
                username = event['UserName']
            except:
                username =''
            try:
                gnoun = event['gnoun']
            except:
                gnoun =''
            try:
                animal = event['animal']
            except:
                animal =''
            try:
                plants = event['plants']
            except:
                plants =''
            try:
                countries = event['countries']
            except:
                countries =''
            try:
                inanimate = event['inanimate']
            except:
                inanimate =''
            try:
                RoomCode = event['RoomCode']
            except:
                RoomCode =''
            try:
                end = event['end']
            except:
                end=False
            try:
                pret =event['pret']
            except:
                pret= False
            try:
                current_letter_this = event['current_letter_this']
            except:
                current_letter_this= None
            try:
                preg=event['preg']
            except:
                preg=False
            try:
                current_letter_this1=event['current_letter_this1']
            except:
                current_letter_this1=None
            try:
                array50=event['array50']
            except:
                array50=None
            try:
                admin_letter=event['admin_letter']
            except:
                admin_letter=None
            try:
                main_row=event['main_row']
            except:
                main_row=True
            try:
                noun_result=event['noun_result']
            except:
                noun_result=None
            try:
                gnoun_result=event['gnoun_result']
            except:
                gnoun_result=None
            try:
                animal_result=event['animal_result']
            except:
                animal_result=None
            try:
                plants_result=event['plants_result']
            except:
                plants_result=None
            try:
                countries_result=event['countries_result']
            except:
                countries_result=None
            try:
                inanimate_result=event['inanimate_result']
            except:
                inanimate_result=None
            try:
                sum=event['sum']
            except:
                sum=None
            try:
                review=event['review']
            except:
                review=False
            try:
                oneortwo=event['oneortwo']
            except:
                oneortwo=False
            try:
                error=event['error']
            except:
                error=False
            try:
                players_game=event['players_game']
            except:
                players_game=False
            try:
                noun_review=event['noun_review']
            except:
                noun_review=False
            try:
                result=event['result']
            except:
                result=False
            try:
                wantletter=event['wantletter']
            except:
                wantletter=False
            try:
                wantletter1=event['wantletter1']
            except:
                wantletter1=False
            try:
                last=event['last']
            except:
                last=False
            try:
                private=event['private']
            except:
                private=False
            try:
                block=event['block']
            except:
                block=False
            try:
                letterconsumer=event['letterconsumer']
            except:
                letterconsumer=False
            try:
                ready=event['ready']
            except:
                ready=False
            try:
                kick=event['kick']
            except:
                kick=False
            try:
                user=event['user']
            except:
                user=""
            try:
                star=event['star']
            except:
                star=False
            try:
                alltables=event['alltables']
            except:
                alltables=False
            try:
                adnan=event['adnan']
            except:
                adnan=False
            try:
                alltables2=event['alltables2']
            except:
                alltables2=False   
            try:
                disabled=event['disabled']
            except:
                disabled=False   

            try:
                kickme=event['kickme']
            except:
                kickme=False 
            try:
                userf=event['userf']
            except:
                userf=False 
            the_letter_choosen = ''
            #print('alllll',alltables)
            if alltables != False:
                self.glabaluser1=str(self.glabaluser)
                #print('شيشي',await (self.see(self.glabaluser1,RoomCode)))
                if True:
                    try:
                        await self.savetable(alltables,self.glabaluser1,RoomCode)
                        await self.delete(RoomCode=RoomCode)
                    except:
                        print('error')

            if alltables2 != False:
                self.glabaluser1=str(self.glabaluser)
                #print('شيشي',await (self.see(self.glabaluser1,RoomCode)))
                if True:
                    try:
                        await self.savetable(alltables2,self.glabaluser1,RoomCode)
                    except:
                        print('error')

            w = await self.save_array(RoomCode,array50)
            t = await self.array(RoomCode)
            await self.send(text_data=json.dumps({ 
                'donnee':t
            }))

            
            
            
            
            #############################
            await self.send(text_data=json.dumps({
                'Noun':noun,
                'gnoun':gnoun,
                'animal':animal,
                'plants':plants,
                'countries':countries,
                'inanimate':inanimate,
                'UserName':username,
                'RoomCode' : RoomCode,
                'end':end,
                'pret':pret,
                'preg':preg,
                'current_letter_this1':current_letter_this1,
                'array50':array50,
                'admin_letter':admin_letter,
                'main_row':main_row,
                'noun_result':noun_result,
                'gnoun_result':gnoun_result,
                'animal_result':animal_result,
                'plants_result':plants_result,
                'countries_result':countries_result,
                'inanimate_result':inanimate_result,
                'sum':sum,
                'review':review,
                'oneortwo':oneortwo,
                'error':error,
                'players_game':players_game,
                'noun_review':noun_review,
                'result':result,
                'wantletter':wantletter,
                'last':last,
                'private':private,
                'block':block,
                'letterconsumer':letterconsumer,
                'ready':ready,
                'kick':kick,
                'user':user,
                'star':star,
                'disabled':disabled,
                'kickme':kickme,
                'userf':userf

                


                
            }))

    @sync_to_async
    def delete(self,RoomCode):
        models.adnan_test11.get(room=RoomCode).delete()
        models.summeryOfLetter.get(room=RoomCode).delete()
        models.array.get(room=RoomCode).delete()
        models.players.get(room=RoomCode).delete()

    @sync_to_async
    def see(self,user,room):
        e=models2.room_created.objects.all().filter(user=user,room_created=room).values()
        #print('we needis',type(e), e)
        e=str(e)
        print('mine',e)
        return e
    @sync_to_async
    def savetable(self,table,y,room):
        models2.room_created.objects.create(user=y,table=table,room_created=room).save()
    @sync_to_async
    def save_array(self,RoomCode,array50):
        models.array(status=array50,room=RoomCode).save()
    @sync_to_async

    def save_info(self ,noun ,gnoun,animal,plants,countries,inanimate,username,the_letter,RoomCode):
        print('adjgeiuolgwhbwk')
        models.adnan_test11.objects.create(noun=noun,gnoun=gnoun,animalNoun=animal,plants=plants,countries=countries,inanimate=inanimate,sum="",user=username,letter=the_letter,room=RoomCode)
    @sync_to_async
    def save(self ,x,RoomCode ):
        x =models.summeryOfLetter(all_letter_as=x,room=RoomCode)
        x.save()
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
    def array(self,RoomCode):
        #print(models.summeryOfLetter.objects.all.order_by('-time').first())

        mydata = models.array.objects.all().filter(room=RoomCode).order_by('-pk').values()
        for i in mydata:
            #global z
            z = i['status']            
            break
        #print('z is ::' , z)
        return z
    @sync_to_async
    def player_save(self,RoomCode,players):
        x =models.players(players=players,room=RoomCode)
        x.save()

    @sync_to_async
    def player(self,RoomCode):
        mydata = models.players.objects.all().filter(room=RoomCode).order_by('-pk').values()
        for i in mydata:
            #global z
            z = i['players']            
            break
        #print('z is ::' , z)
        
        return z        

    def infit(self):
        print('infinity')
    @sync_to_async
    def thisis(self,player_this,room_this):
        from accounts.models import played
        played.objects.create(user=player_this,room_played=room_this).save()
        print('romeinoedef',player_this,room_this)
    @sync_to_async
    def alltabels2(self,user,room,all):
        from.models import room_created
        room_created.objects.create(user=user,table=all,room_created=room).save()