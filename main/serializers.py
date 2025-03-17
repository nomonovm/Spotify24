from rest_framework import serializers
from .models import *

class QoshiqchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiqchi
        fields = '__all__'

class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = '__all__'

class QoshiqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = '__all__'

    def validate_fayl(self, value):
        if value and not value.name.endswith('.mp3'):
            raise serializers.ValidationError("Qo'shiq fayli faqat '.mp3' formatda bo‘lishi kerak.")
        return value

    def validate_davomiylik(self, value):
        if value and value.total_seconds() > 7 * 60:
            raise serializers.ValidationError("Qo'shiq davomiyligi 7 daqiqadan oshmasligi kerak.")
        return value
