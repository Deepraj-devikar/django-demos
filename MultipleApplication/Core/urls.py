from django.urls import include, path
from .views import *

urlpatterns = [
    path('course/', include('Course.urls')),
    path('fees/', include('Fees.urls')),
    path('<str:unknown>/', unknown, name="unknown")
]