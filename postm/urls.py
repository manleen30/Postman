from django.urls import path
from postm import views

urlpatterns=[
    path('postm/',views.todo_list),
     path('todo/<int:pk>/', views.todo_detail),
]