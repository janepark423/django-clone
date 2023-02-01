from django.conf import settings
from django.db import models


# Create your models here.
class myText(models.Model) :
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)

    def publish(self):
        self.save()
    def __str__(self):
        return self.title