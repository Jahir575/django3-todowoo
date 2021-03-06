"""todowoo URL Configuration

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
from todo import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.signupuser, name="signup"),
    path('logout/', views.logoutuser, name="logout"),
    path('login/', views.loginuser, name="login"),

    # Todo
    path('', views.home, name = "home"),
    path('createtodo/', views.createtodo, name="createtodo"),
    path('currenttodos/', views.currenttodos, name="currenttodos"),
    path('viewtodo/<int:todo_pk>', views.viewtodo, name="viewtodo"),
    path('viewtodo/<int:todo_pk>/completedtodo', views.completedtodo, name="completedtodo"),
    path('viewtodo/<int:todo_pk>/deletetodo', views.deletetodo, name="deletetodo"),
    path('completedtodolist/', views.completedtodolist, name="completedtodolist"),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
