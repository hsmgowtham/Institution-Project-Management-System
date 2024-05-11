from django.urls import path

from . import views

urlpatterns = [
    # path('', views.api_home),
    path('<int:pk>/', views.StudentDetailAPIView.as_view()),
    path('', views.StudentListCreateAPIView.as_view()),
    path('<int:pk>/update/', views.StudentUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.StudentDestroyAPIView.as_view()),
]