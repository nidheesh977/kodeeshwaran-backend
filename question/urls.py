from django.urls import path
from . import views

app_name = "question"

urlpatterns = [
  path("", views.QuestionListCreateView.as_view(), name = "question_list_create_view"),
  path("detail/<str:pk>/", views.QuestionDetailView.as_view(), name = "question_detail_view"),
  path("options/", views.OptionListCreateView.as_view(), name = "option_list_create_view"),
  path("options/detail/<str:pk>/", views.OptionDetailView.as_view(), name = "option_detail_view"),
]