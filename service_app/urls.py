from django.urls import path

from .views import health_check, ValentineList, ValentineRetrieve, UserRetrieve, UserList

urlpatterns = [
    path('ping/', health_check),
    path('valentines/', ValentineList.as_view()),
    path('valentine/<int:pk>/', ValentineRetrieve.as_view()),
    path('users/', UserList.as_view()),
    path('user/<int:pk>/', UserRetrieve.as_view()),
]