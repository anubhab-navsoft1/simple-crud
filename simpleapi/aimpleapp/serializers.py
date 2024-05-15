from rest_framework import serializers
from .models import SampleUser


class SampleUSerSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = SampleUser
        fields = ['name', 'email', 'age', 'account']
        read_only_fields = ['id']