from django.urls import path
from topics import views

urlpatterns = [
    path('topics/', views.TopicsList.as_view()),
    path('topics/<int:pk>/', views.TopicsDetail.as_view()),
]
