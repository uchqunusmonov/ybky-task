from django.urls import path
from . import views


urlpatterns = [
    path('rooms/', views.RoomListView.as_view(), name='rooms_list'),
    path('rooms/<int:pk>/', views.RoomDetailView.as_view(), name='room_detail'),
]