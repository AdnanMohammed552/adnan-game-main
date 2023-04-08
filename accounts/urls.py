from django.urls import path
from .import views
from animal import views as v
urlpatterns = [
    path('signup', views.signup),
    path('login',views.login),
    path('logout',views.logout , name="logout"),
    path('game/myaccount',views.mygames),
    path('game',views.created),
    path('game/quiz',views.quiz),
    path('game/quiz/<int:room_code>/',views.quiz_data),
    path('game/quiz/<int:room_code>/start',v.room_admin_quiz),
    path('game/quiz/<int:room_code>/startqr',v.room_admin_quiz_qr),
    
    path('home',views.home),
    path('played',views.played),
    path('played/<int:room_code>/',views.playedacc),

    path('myaccount/<int:room_code>/',views.myaccount),
    path('qrcodes',views.qrcodes)

]