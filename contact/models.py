from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/')
    terms_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
