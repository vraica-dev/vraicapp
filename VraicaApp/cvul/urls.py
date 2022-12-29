from django.urls import path
from .views import home, cv_page


urlpatterns = [
    path('', home, name='home-cv'),
    path('cv/', cv_page, name='cv-page')
]
