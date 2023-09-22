from rest_framework import serializers
from .models import  database
class databaseSerializer(serializers.Serializer):
    teacher_name= serializers.CharField(max_length=100)
    course_name = serializers.CharField(max_length=100)
    course_duration = serializers.IntegerField()
    seat= serializers.IntegerField()

#to recieve json and convert into compkex or database table
def create(self, validated_data):
    return database.objects.create(**validated_data)