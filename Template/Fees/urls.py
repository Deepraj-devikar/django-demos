from django.urls import path
from .views import *

urlpatterns = [
    path('django/', django),
    path('node/', node),
    path('<str:unknown>/<str:fees>', unknown),
]
