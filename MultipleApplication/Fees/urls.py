from django.urls import path
from .views import *

urlpatterns = [
    path('django/', django, name="django_fees"),
    path('node/', node, name="node_fees"),
    path('<str:unknown>/', unknownFees, name="unknown_fees"),
    path('<str:unknown>/<str:fees>/', unknownFees, name="unknown_fees"),
]