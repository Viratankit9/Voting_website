from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Party(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='party_logos/')

    def __str__(self):
        return self.name

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} voted for {self.party.name}"