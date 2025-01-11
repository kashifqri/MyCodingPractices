from django.db import models
class Service(models.Model):
    service_icon = models.ImageField(upload_to='service_icons/') 
    service_title = models.CharField(max_length=50)
    service_des = models.TextField()

    def __str__(self):
        return self.service_title


# Create your models here.
