from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room_page/<str:pk>/', views.room, name="room"),

    path('room-create/', views.create_room, name="create_room"),
    path('room-update/<str:pk>/', views.update_room, name="update_room"),
    path('delete-room/<str:pk>', views.delete_room, name='delete_room')
]
