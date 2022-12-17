from django.urls import path
from .views import *

urlpatterns = [
    path('django/', django, name="django_course"),
    path('node/', node, name="node_course"),
    path('<str:unknown>/', unknownCourse, name="unknown_course"),
]