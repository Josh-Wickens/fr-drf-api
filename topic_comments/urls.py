from django.urls import path
from topic_comments import views

urlpatterns = [
    path('topic_comments/', views.TopicCommentList.as_view()),
    path('topic_comments/<int:pk>/', views.TopicCommentDetail.as_view())
]
