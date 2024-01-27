from django.urls import path
from .views import *
urlpatterns = [
    path('',sign_in,name="sign_in"),
    path('sign_up/',sign_up,name="sign_up"),
    path('sign_out/',sign_out,name="sign_out"),
    path('home/',home,name="home"),
    path('profile/',profile,name="profile"),


]
