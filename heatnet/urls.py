"""
URL configuration for heatnet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from heatnet_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create-project/', views.create_project, name='create_project'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('proj/', views.proj, name='proj'),  # URL для першого шаблону
    path('proj-detail/', views.proj_detail, name='proj_detail'),  # URL для другого шаблону
    path('proj-list/', views.proj_list, name='proj_list'),  # URL для третього шаблону
    path('node/', views.node_view, name='node'),  # URL для четвертого шаблону
    path('links/', views.links_view, name='links'),  # URL для п'ятого шаблону
]
