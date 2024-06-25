from django.urls import path
from.import views

urlpatterns = [
    path('',views.roomentering , name='room'),
    path('create',views.create),
    path('activity',views.activity),

    path('create/type',views.type),
    path('<int:room_code>/' , views.room ),
    path('join/<int:room_code>/' , views.joinnow ),
    path('joinquiz/<int:room_code>/' , views.joinquiz ),
    path('joinquiz' , views.join_quiz ),

    path('wait/<int:room_code>/' , views.wait),
    path('waitquiz/<int:room_code>/' , views.wait_quiz),

    path('end/<int:room_code>/' , views.end),
    path('<int:room_code>/admin' , views.room_admin ),
    path('<int:room_code>/quizadmin' , views.room_admin_quiz ),
    path('<int:room_code>/admin/end' , views.room_end ),
    path('quiz',views.quiz),
    path('api/endpoint/', views.req, name='my-endpoint'),
    path('api/endpoint1/', views.req1, name='my-endpoint'),
    path('api/endpoint2/', views.arabic, name='my-endpoint'),
    path('api/endpoint5/', views.delete, name='my-endpoint'),
    path('api/endpointpass/', views.password, name='my-endpoint'),
    path('api/endpoint_restore/', views.endpoint_restore, name='my-endpoint'),
    path('api/endpoint_reeset/', views.endpoint_reeset, name='my-endpoint'),
    path('play/<int:room_code>', views.play, name='playy'),
    path('managment/<int:room_code>',views.managment),
    path('api/endpointpassword/', views.endpointpassword, name='my-endpoint'),
    path('api/red/', views.red, name='my-endpoint'),

    path('camera_manage/<int:room_code>/', views.process_form, name='camera_manage'),

    path('playing/<int:room_code>/start', views.process_form_play, name='playing'),
    path('playing/<int:room_code>/', views.quiz_details, name='playing'),


    path('join',views.join),
    path('joinqr/<int:room_code>',views.joinqr),
    path('camera/<int:room_code>',views.camera),

    

]