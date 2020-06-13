from rest_framework import serializers

from .models import BoilerPlateCode

class BoilerPlateCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoilerPlateCode
        fields = ('language', 'boilerPlate')