from django.urls import path

from . import views

urlpatterns = [
    # path('', views.api_home),
    path('<int:pk>/', views.FacultyDetailAPIView.as_view()),
    path('', views.FacultyListCreateAPIView.as_view()),
    path('<int:pk>/update/', views.FacultyUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.FacultyDestroyAPIView.as_view()),
]