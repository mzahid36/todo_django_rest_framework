from django.urls import path
from .views import *

urlpatterns = [
    path('',apiOverView),
    path('task-list/',TaskList,name='task-list'),
    path('task-detail/<str:pk>/',TaskDetail,name='task-detail'),
    path('task-create/',TaskCreate,name='task-create'),
    path('task-update/<str:pk>/',TaskUpdate,name='task-update'),
    path('task-delete/<str:pk>/',TaskDelete,name='task-Delete'),
]