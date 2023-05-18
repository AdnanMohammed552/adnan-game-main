from django.contrib import admin

# Register your models here.
from .models import title,MyModel,priv,room_created,password,enumeration,played_quiz,total_score,enumeration_played
admin.site.register(title)
admin.site.register(MyModel)
admin.site.register(priv)
admin.site.register(room_created)
admin.site.register(password)
admin.site.register(enumeration)
admin.site.register(total_score)
admin.site.register(enumeration_played)
admin.site.register(played_quiz)


