from django.urls import path
from .views import home, cv_page, download_cv

from rest_framework.routers import DefaultRouter
from .views import CVViewset

router = DefaultRouter()
router.register(r'api/cvdoc', CVViewset, basename='cvapi')

urlpatterns = [
    path('', home, name='home-cv'),
    path('cv/', cv_page, name='cv-page'),
    path('download/', download_cv, name='download-cv')
] + router.urls

