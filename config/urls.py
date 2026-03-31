"""dream_lab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from dream_core.health_check.views import health_check_view


api_v1_patterns = [
    # path('test/',     include('dream_lab.accounts.urls.auth')),
]

urlpatterns = [
    path('health-check/', health_check_view),
    path('api/lab/v1/', include(api_v1_patterns)),
]