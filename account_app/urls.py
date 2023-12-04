from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('enterphone', views.enter_phone, name='enter_phone'),
    path('entercode', views.enter_code, name='enter_code'),
    path('signin', views.signin, name='signin'),
    path('sendagain', views.send_again, name='sendagain'),
    path('home', views.home, name='home'),

]