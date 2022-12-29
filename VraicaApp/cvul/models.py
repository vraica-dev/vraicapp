from django.db import models

# Create your models here.
class CVApiKey(models.Model):

    cvkey = models.CharField(max_length=250, default='missing')
    used = models.BooleanField(default=False, null=False)
    used_on = models.DateTimeField(auto_created=True)

