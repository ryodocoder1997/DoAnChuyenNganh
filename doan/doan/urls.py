"""doan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', TemplateView.as_view(template_name='base.html')),
    path('homepage', TemplateView.as_view(template_name='homePage.html')),
    path('user', TemplateView.as_view(template_name='user-profile.html')),
    path('businesss', TemplateView.as_view(template_name='business.html')),
    path('tutorlist', TemplateView.as_view(template_name='tutorList.html')),
    path('courselist', TemplateView.as_view(template_name='courseList.html')),
    path('academylist', TemplateView.as_view(template_name='academyList.html')),
    path('termofuses', TemplateView.as_view(template_name='term-of-uses.html')),
    path('navuser', TemplateView.as_view(template_name='header-user-profile.html')),

]
