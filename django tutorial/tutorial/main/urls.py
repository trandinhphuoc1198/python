
from . import views
from django.urls import path

urlpatterns = [
    path('', views.room,name="home"),
    path('room/', views.room,name="room"),
    path('room/<str:pk>/', views.room),
    path('create_room',views.create_room,name='create_room'),
    path('update_room/<str:pk>',views.update_room,name='update_room'),
    path('delete_room/<str:pk>',views.delete_room,name='delete_room'),
    path('log_in',views.log_in,name='log_in'),
    path('log_out',views.log_out,name='log_out'),
    path('register',views.register,name='register'),
    path('delete_message/<str:pk>',views.delete_message,name='delete_message')
]
