from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.starter,name='mwanzo'),
    path('speaker/',views.speaker,name='ongea'),
]
