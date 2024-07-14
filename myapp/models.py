from django.db import models

class Contact_us(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
   

    def str(self):
        return self.name