import os
import datetime
from .models import CVApiKey, CVDocument
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404
from django.contrib import messages

from rest_framework import viewsets
from .serializers import CVDocSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser


def home(request):
    return render(request, "cvul/home.html")


def cv_page(request):
    """
    the main page where the recruiter can download the cv;
    a CVKey is necessary for being able to download the pdf file;
    """
    if request.method == 'POST':
        received_key = request.POST.get('inputCvKey')
        if received_key:
            try:
                crr_key = CVApiKey.objects.get(cvkey=received_key)

                if crr_key.used:
                    messages.error(request, "CV Key already exists. Please request a new one.")
                    return render(request, 'cvul/cv.html', context={"downloadready": False})

                crr_key.used = True
                crr_key.used_on = datetime.datetime.now()
                crr_key.save()
            except CVApiKey.DoesNotExist:
                messages.info(request, "CV Key invalid. Please try another one.")
                return render(request, 'cvul/cv.html')
            else:
                print("DOWNLOAD")
                return render(request, 'cvul/cv.html', context={"downloadready": True})

    return render(request, "cvul/cv.html")


def download_cv(request):
    """
    serves the CV as pdf file if exists;
    """
    cv_path = os.path.join(settings.MEDIA_ROOT, 'test_empty.pdf')
    if os.path.exists(cv_path):
        with open(cv_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + \
                os.path.basename(cv_path)
            return response
    raise Http404


class CVViewset(viewsets.ViewSet):
    
    def list(self, request):
        queryset = CVDocument.objects.all()
        serializer = CVDocSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = CVDocument.objects.all()
        serializer = CVDocSerializer(queryset, many=True)
        return Response(serializer.data)


        

    # def get_permissions(self):
    #     if self.action == 'retrieve':
    #         permission_classes = [IsAuthenticated]
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]