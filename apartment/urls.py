from django.urls import path

from . import views


urlpatterns = [
    path('', views.ApartmentListCreateAPIView.as_view()),
    path('<int:pk>/', views.ApartmentRetrieveUpdateDestroyAPIView.as_view()),
    path('city/', views.CityListAPIView.as_view()),
]