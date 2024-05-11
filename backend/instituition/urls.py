from django.urls import path

from . import views

urlpatterns = [
    # path('', views.api_home),
    path('<int:pk>/', views.InstituitionDetailAPIView.as_view()),
    path('', views.InstituitionListCreateAPIView.as_view()),
    path('<int:pk>/update/', views.InstituitionUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.InstituitionDestroyAPIView.as_view()),
]