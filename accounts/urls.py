from django.urls import path
from .import views
urlpatterns = [
    path('signup', views.signup),
    path('login',views.login),
    path('logout',views.logout , name="logout"),
    path('myaccount',views.mygames),
    path('home',views.home),
    path('played',views.played),
    path('played/<int:room_code>/',views.playedacc),

    path('myaccount/<int:room_code>/',views.myaccount)
]