from rest_framework import serializers
from .models import Contact, SpamMark

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone_number', 'email']

class SpamMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamMark
        fields = ['id', 'phone_number', 'marked_by']
