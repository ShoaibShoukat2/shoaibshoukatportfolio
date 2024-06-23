from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index-page"),
    path('blogs/',blogs,name="blogs-page"),
    path('django-first-app/',djangoFirstApp,name="djangoFirstApp-page"),
    path('event-site/',eventsite,name="evenet-website"),
    path('fui-site/',FuiSite,name="fui-website")

]
