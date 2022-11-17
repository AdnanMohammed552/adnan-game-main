from django.urls import path
from.import views

urlpatterns = [
    path('',views.roomentering , name='room'),
    path('create',views.create),
    path('<int:room_code>/' , views.room ),
    path('join/<int:room_code>/' , views.joinnow ),
    path('wait/<int:room_code>/' , views.wait),
    path('end/<int:room_code>/' , views.end),
    path('<int:room_code>/admin' , views.room_admin ),
    path('<int:room_code>/admin/end' , views.room_end ),

    path('join',views.join),
    path('joinqr/<int:room_code>',views.joinqr)

]