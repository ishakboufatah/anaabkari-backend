"""anaabkari URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from rest_framework import routers
from database.views import ClaseViewSet,SubjectsPrimary1ViewSet,SubjectsPrimary2ViewSet,USERViewSet

router = routers.DefaultRouter()
router.register(r'Clase',ClaseViewSet,basename='Clase')
router.register(r'SubjectsPrimary1',SubjectsPrimary1ViewSet,basename='SubjectsPrimary1')
router.register(r'SubjectsPrimary2',SubjectsPrimary2ViewSet,basename='SubjectsPrimary2')
router.register(r'USER',USERViewSet,basename='Clase')


urlpatterns = [
    path('',include(router.urls)), 
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [

  url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

  url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]