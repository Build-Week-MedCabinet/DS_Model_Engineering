"""djapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from djapi.recommender import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'strains', views.StrainViewSet)
router.register(r'userratings', views.UserRatingViewSet)  # Not implemented in model.

# Wire up API using automatic URL routing
# Additionally, including login URLs for the browsable API
urlpatterns = [
    path('', include(router.urls)),
    path('recommend/', views.recommender_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]