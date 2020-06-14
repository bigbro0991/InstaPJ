"""Instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Insta.views import (HelloWorld,PostsListView,PostsDetailView,PostsCreateView,
                         PostsUpdateView,PostsDeleteView)

urlpatterns = [
    path('', HelloWorld.as_view(),name='helloword'),  
    path('posts/', PostsListView.as_view(),name='posts'),  
    path('post/<int:pk>/', PostsDetailView.as_view(), name='posts_detail'),
    path('posts/new/', PostsCreateView.as_view(), name='make_post'),
    path('posts/update/<int:pk>', PostsUpdateView.as_view(), name='update_post'),
    path('posts/delete/<int:pk>', PostsDeleteView.as_view(), name='delete_post'),
]
