from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes,name='routes'),
    path('messages/',views.getMessages, name='messages'),
    path('messages/create/',views.uploadMessage, name='upload-message'),
    path('messages/delete/<str:pk>/', views.deleteMessage, name='delete-message'),
]