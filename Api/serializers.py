from rest_framework import serializers

# Create your serializers here.
class StudentSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    roll=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    city=serializers.CharField(max_length=200)

