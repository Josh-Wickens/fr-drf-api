from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.LikeList.as_view()),
    path('likes/<int:pk>/', views.LikeDetail.as_view()),
    path('likes-topic/', views.LikeTopicList.as_view()),
    path('likes-topic/<int:pk>/', views.LikeTopicDetail.as_view()),
    path('likes-topic-comment/', views.LikeTopicCommentList.as_view()),
    path('likes-topic-comment/<int:pk>/', views.LikeTopicCommentDetail.as_view()),
]