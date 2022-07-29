from pyexpat import model
from .models import *
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuesForm
        fields = '__all__'
        