"""URLDispatcher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, register_converter

from CreateURL import views as createURL
from CreateURL import converters

register_converter(converters.FourDigitYearConverter, "yyyy")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome_to_home/<str:val>', createURL.welcome_to_home, name="welcome_to_home_name"),
    path('welcome/<str:val>', createURL.welcome, name="welcome_name"),
    path('detail/', createURL.show_details, {"check": "OK"}, name="detail"),
    path('detail/<my_id>/', createURL.show_details, {"check": "OK"}, name="detail"),
    path('detail/<my_id>/<my_subid>', createURL.show_subdetails, {"check": "OK"}, name="detail"),
    path('home/', createURL.home, name="home"),
    path('session/<yyyy:year>', createURL.show_year, name="show_year")
]
