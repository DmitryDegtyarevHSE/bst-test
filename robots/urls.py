from django.urls import path
from .import views

urlpatterns = [
    path('add/', views.RobotView.as_view(), name="robot-view"),
    path('download/', views.download_excel, name="download-excel")
]
