from django.core.management.base import BaseCommand
from contacts.models import Contact, SpamMark
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        user = User.objects.create_user('testuser', password='testpass')
        for i in range(100):
            contact = Contact.objects.create(
                user=user,
                name=f'Contact{i}',
                phone_number=f'123456789{i}',
            )
            if random.choice([True, False]):
                SpamMark.objects.create(phone_number=contact.phone_number, marked_by=user)
