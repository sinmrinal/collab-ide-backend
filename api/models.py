from django.db import models


class RoomInfo(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    joined_by = models.CharField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
