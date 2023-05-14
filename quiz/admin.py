from django.contrib import admin

# Register your models here.
from .models import title,MyModel,priv,room_created,password,enumeration,played_quiz
admin.site.register(title)
admin.site.register(MyModel)
admin.site.register(priv)
admin.site.register(room_created)
admin.site.register(password)
admin.site.register(enumeration)
admin.site.register(played_quiz)


