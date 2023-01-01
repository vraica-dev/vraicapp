from django.db import models
import datetime


class CVApiKey(models.Model):
    cvkey = models.CharField(max_length=250, default='missing')
    used = models.BooleanField(default=False)
    used_on = models.DateTimeField(auto_created=True, null=True)

    def __str__(self) -> str:
        return self.cvkey


class CVDocument(models.Model):
    name = models.CharField(max_length=250, default="Valentin Raica")
    phone = models.CharField(max_length=13, null=True, blank=True)
    age = models.IntegerField(blank=True, null=True, default=30)
    current_position = models.CharField(max_length=250, null=True, blank=True)
    months_on_position = models.IntegerField(blank=True, null=True)
    previous_jobs = models.JSONField(default=[])
    last_studies = models.CharField(max_length=250, blank=True, null=True)
    stack = models.JSONField(default=dict)
    hobbies = models.JSONField(default=[])
    cv_last_update = models.DateField(default=datetime.datetime.now())


