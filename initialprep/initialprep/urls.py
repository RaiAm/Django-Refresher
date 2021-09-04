"""initialprep URL Configuration

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
from os import stat
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), #home - first redirect to the url
    path('about/', views.about, name='about'),  #about page redirect
    path('removepunc/', views.removepunc, name='removepunc'),
    path('blog/', include('blog.urls')),

    # If a new app is there we can include in main project to refer to url request to that app specifically
    # path('<name of the app>/', include('<name of the app>.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
