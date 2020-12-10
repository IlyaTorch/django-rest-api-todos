from django.urls import path
from . import views

urlpatterns = [
    # Todos
    path('todos', views.TodoCreateList.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', views.TodoComplete.as_view()),
    path('todos/completed', views.TodoCompletedList.as_view()),

    # Auth
    path('signup', views.sing_up),
    path('login', views.login_user),
]
