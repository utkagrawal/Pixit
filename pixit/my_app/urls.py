from django.urls import path
from . import views


app_name= 'my_app'

urlpatterns=[
    path("",views.IntroPageView, name='intro'),
    path("home/", views.HomePageView, name='homepage'),
    path("loading/",views.LoadView, name='loading'),
    path('result/',views.ResultView, name='result'),
    path('sample/', views.ExampleView, name='sample'),
    path('about/',views.AboutView, name='about')
    

]