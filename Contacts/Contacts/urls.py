"""
URL configuration for Contacts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Contact import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('html/add', views.html_add, name='contact_form'),
    path('add/save', views.html_add_save, name='save_contact'),
    path('html/edit', views.html_edit, name='edit_form'),
    path('edit/save', views.html_edit_save, name='edit_contact'),
    path('html/read', views.html_read, name='read'),
    path('html/delete', views.html_delete, name='delete'),
]
