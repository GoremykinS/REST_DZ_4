"""backend URL Configuration
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from library.views import AuthorViewSet, get_view, post_view, BookViewSet, BioViewSet
from todo.views import ProjectViewSet, get_view2, post_view2, TodoViewSet

router = DefaultRouter()
router.register('authors', AuthorViewSet, basename='authors')
router.register('Project', ProjectViewSet, basename='projects')
router.register('Todo', TodoViewSet, basename='Todos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api_get/', get_view),
    path('api_post/', post_view),
    path('api_get2/', get_view2),
    path('api_post2/', post_view2),
    # path('api_get/<str:first_name>/', AuthorViewSet.as_view({'get': 'list'})),
    # path('api_get/<int:pk>/', AuthorViewSet.as_view({'get': 'retrieve'})),
    # path('api_get/', get_view),
    # path('api_post/', post_view)
]



