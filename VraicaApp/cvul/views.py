from django.shortcuts import render
from .models import CVApiKey
from .forms import CvKeyForm


def home(request):
    return render(request, "cvul/home.html")


def cv_page(request):
    return render(request, "cvul/cv.html")
