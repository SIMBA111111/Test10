from django.urls import path

from gh import views

urlpatterns = [
    path('get-gh', views.GettingDataFromGithub.as_view(), name='get-gh'),
]
