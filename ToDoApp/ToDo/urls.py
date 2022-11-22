from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.taskList.as_view()),
    #path('complete-view/',views.completedTask.as_view()),
    path('marked-view/',views.markedComplete.as_view()),
    path('delete/<int:pk>/', views.deleteTask.as_view()),
]