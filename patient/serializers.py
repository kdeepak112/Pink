from rest_framework import serializers
from .models import diseaseApi,mumbai,pune , labBook,PatientMessage
from doctor.models import Message


class diseaseSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = diseaseApi
        fields = '__all__'

class mumbaiSerializer(serializers.ModelSerializer):

    class Meta :
        model = mumbai
        fields = '__all__'

class puneSerializer(serializers.ModelSerializer):

    class Meta :
        model = pune
        fields = '__all__'

class labBookSerializer(serializers.ModelSerializer):

    class Meta :
        model = labBook
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):

    class Meta :
        model = Message
        fields = '__all__'

class PatientMessageSerializer(serializers.ModelSerializer):

    class Meta :
        model = PatientMessage
        fields = '__all__'