from django.db import models

class BoilerPlateCode(models.Model):
    language = models.CharField(max_length=10)
    boilerPlate = models.CharField(max_length=200)

    def __str__(self):
        return f'Language: {self.language}'

    class Meta:
        db_table = 'BoilerPlateCode'
