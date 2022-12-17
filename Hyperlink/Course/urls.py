from django.urls import path
from .views import *
urlpatterns = [
    path('all/', allCourses, name="allCourses"),
    path('django/', django, name="djangoCourse"),
    path('node/', node, name="nodeCourse"),
]
