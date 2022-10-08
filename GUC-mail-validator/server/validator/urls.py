from django.urls import path
from .views import Validator
urlpatterns = [
    path('', Validator.as_view())
]
