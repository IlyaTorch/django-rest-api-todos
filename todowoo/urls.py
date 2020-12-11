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
from django.urls import path, include
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.sign_up_user, name='sign-up-user'),
    path('login/', views.login_user, name='login-user'),
    path('logout/', views.logout_user, name='logout-user'),

    # Todos
    path('', views.home, name='home'),
    path('create/', views.create_todo, name='create-todo'),
    path('current/', views.current_todos, name='current-todos'),
    path('completed/', views.completed_todos, name='completed-todos'),
    path('todo/<int:todo_pk>', views.view_todo, name='view-todo'),
    path('todo/<int:todo_pk>/complete', views.complete_todo, name='complete-todo'),
    path('todo/<int:todo_pk>/delete', views.delete_todo, name='delete-todo'),

    # API
    path('api/', include('api.urls'))
]
