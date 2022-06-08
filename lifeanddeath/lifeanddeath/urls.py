"""lifeanddeath URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path

import main.views

urlpatterns = [
    path('', main.views.index),
    path('<str:path>', main.views.text),
    re_path(r'^(?i)denn', main.views.denn),
    re_path(r'^(?i)für', main.views.für),
    re_path(r'^(?i)fuer', main.views.für),
    re_path(r'^(?i)mich', main.views.mich),
    re_path(r'^(?i)ist', main.views.ist),
    re_path(r'^(?i)christus', main.views.christus),
    re_path(r'^(?i)das', main.views.das),
    re_path(r'^(?i)leben', main.views.leben),
    re_path(r'^(?i)und', main.views.und),
    re_path(r'^(?i)sterben', main.views.sterben),
    re_path(r'^(?i)ein', main.views.ein),
    re_path(r'^(?i)gewinn', main.views.gewinn),
    path('admin/', admin.site.urls),
]
