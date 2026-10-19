from django.urls import path
from .views import QuestionListAPIView,QuestionSubmitAPIView,QuestionStatsAPIView
urlpatterns=[path('',QuestionListAPIView.as_view()),path('submit/',QuestionSubmitAPIView.as_view()),path('stats/',QuestionStatsAPIView.as_view())]
