from django.urls import path
from . import views

urlpatterns = [
    path('users/create/', views.CreateSampleUser.as_view(), name= 'create'),
    path('users/', views.ListOfUsers.as_view(), name= 'list')
]

