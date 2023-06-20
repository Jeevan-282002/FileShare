from django.urls import path
from .import views

urlpatterns = [
    path('handle/',views.HandleFileUpload.as_view()),
    path('',views.Home_view.as_view(),name ='Home'),
    path('download/<uid>/',views.download ,name='download'),
    ]