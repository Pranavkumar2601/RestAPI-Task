from rest_framework import viewsets
from .models import Contact, SpamMark
from .serializers import ContactSerializer, SpamMarkSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class SpamMarkViewSet(viewsets.ModelViewSet):
    queryset = SpamMark.objects.all()
    serializer_class = SpamMarkSerializer
