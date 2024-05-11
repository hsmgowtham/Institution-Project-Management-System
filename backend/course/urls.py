from django.urls import path

from . import views

urlpatterns = [
    # path('', views.api_home),
    path('<str:pk>/', views.CourseDetailAPIView.as_view()),
    path('', views.CourseListCreateAPIView.as_view()),
    path('<int:pk>/update/', views.CourseUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.CourseDestroyAPIView.as_view()),
]