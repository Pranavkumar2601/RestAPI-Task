from django.db import models
from django.contrib.auth.models import User
# from contacts.models import Contact 

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

# class SpamMark(models.Model):
#     phone_number = models.CharField(max_length=15)
#     marked_by = models.ForeignKey(User, on_delete=models.CASCADE)
class SpamMark(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    marked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number
