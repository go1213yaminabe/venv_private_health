from django.urls import path
from . import views

app_name = 'health'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    #path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    #path('', views.HealthListView.as_view(), name="health_list"),
    path('health-detail/<int:pk>/', views.HealthDetailView.as_view(), name="health_detail"),
    path('health-create/', views.HealthCreateView.as_view(), name="health_create"),
    path('health-update/<int:pk>/', views.HealthUpdateView.as_view(), name="health_update"),
    path('health-delete/<int:pk>/', views.HealthDeleteView.as_view(), name="health_delete"),
]