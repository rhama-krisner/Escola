from rest_framework import serializers
from .models import Aluno, Curso

class Aluno_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class Curso_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
