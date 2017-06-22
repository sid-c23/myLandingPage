from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.email