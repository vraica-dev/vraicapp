from django.urls import path
from .views import home, cv_page, download_cv


urlpatterns = [
    path('', home, name='home-cv'),
    path('cv/', cv_page, name='cv-page'),
    path('download/', download_cv, name='download-cv')
]
