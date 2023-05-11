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
    path('game/quiz/<int:room_code>/last',views.quiz_data_last),
    path('game/quiz/<int:room_code>/last/<int:id>',views.quiz_data_last_preview),


    path('game/quiz/<int:room_code>/start',v.room_admin_quiz),
    path('game/quiz/<int:room_code>/edit',v.edit),

    path('game/quiz/<int:room_code>/startqr',v.room_admin_quiz_qr),
    path('game/quiz/<int:room_code>/view_questions',v.view_questions),

    path('game/quiz/<int:room_code>/startqr/end/<int:id>',v.room_admin_quiz_qr_end),

    
    path('home',views.home),
    path('played',views.played),
    path('played/<int:room_code>/',views.playedacc),

    path('myaccount/<int:room_code>/',views.myaccount),
    path('qrcodes',views.qrcodes)

]