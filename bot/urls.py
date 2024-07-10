from django.urls import path
from . import views

urlpatterns = [
    path('', views.telegram_bot, name='telegram_bot'),
    path('setwebhook/', views.setwebhook, name='setwebhook'),
]