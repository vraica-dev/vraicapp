from django.shortcuts import render
from .models import CVApiKey


def home(request):
    return render(request, "cvul/home.html")


def cv_page(request):
    if request.method == 'POST':
        received_key = request.POST.get('inputCvKey')
        if received_key:
            try:
                crr_key = CVApiKey.objects.get(cvkey=received_key)
            except CVApiKey.DoesNotExist:
                return render(request, 'cvul/home.html')
            else:
                print("DOWNLOAD")
                return render(request, 'cvul/cv.html', context={"downloadready": True})

    return render(request, "cvul/cv.html")
