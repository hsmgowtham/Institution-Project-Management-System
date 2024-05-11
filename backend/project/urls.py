from django.urls import path

from . import views

urlpatterns = [
    # path('', views.api_home),
    path('<str:pk>/', views.ProjectDetailAPIView.as_view()),
    path('', views.ProjectListCreateAPIView.as_view()),
    path('<int:pk>/update/', views.ProjectUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ProjectDestroyAPIView.as_view()),
]