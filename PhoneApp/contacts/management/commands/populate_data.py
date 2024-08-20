# from django.core.management.base import BaseCommand
# from contacts.models import Contact, SpamMark
# from django.contrib.auth.models import User
# import random

# class Command(BaseCommand):
#     help = 'Populate the database with test data'

#     def handle(self, *args, **kwargs):
#         user = User.objects.create_user('testuser', password='testpass')
#         for i in range(100):
#             contact = Contact.objects.create(
#                 user=user,
#                 name=f'Contact{i}',
#                 phone_number=f'123456789{i}',
#             )
#             if random.choice([True, False]):
#                 SpamMark.objects.create(phone_number=contact.phone_number, marked_by=user)
from django.core.management.base import BaseCommand
from contacts.models import Contact, SpamMark
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Populate the database with random sample data'

    def handle(self, *args, **kwargs):
        # Ensure at least one user exists
        if not User.objects.exists():
            user = User.objects.create_user(username='testuser', password='password')
        else:
            user = User.objects.first()

        # Create sample contacts
        for i in range(10):
            contact = Contact.objects.create(
                name=f'Contact {i}',
                phone_number=f'+1234567890{i}',
                email=f'contact{i}@example.com',
                user=user
            )
            self.stdout.write(self.style.SUCCESS(f'Created contact {contact.name}'))

        # Create sample spam marks
        for i in range(5):
            spam_mark = SpamMark.objects.create(
                contact=Contact.objects.order_by('?').first(),
                marked_by=user
            )
            

            self.stdout.write(self.style.SUCCESS(f'Created spam mark for {spam_mark.contact.name}'))
