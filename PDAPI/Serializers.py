from .models import Subjects
from rest_framework import serializers

class SubjectsSerializers(serializers.ModelSerializer):
    doc = serializers.FileField(max_length=None, use_url=True)

    class Meta:
        model = Subjects
        fields = ('id', 'Patient_name', 'date_created', 'doc')