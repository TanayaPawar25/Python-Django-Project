from django.contrib import admin
from django.urls import path, include
from home import views

from django.views.static import serve
from django.conf.urls import url 

urlpatterns = [ 
    path('',views.index, name="home"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

