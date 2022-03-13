from django.db import models

# Create your models here.
class UserData(models.Model):
    Name_of_party = models.CharField(max_length=50)
    Industry = models.TextField(max_length=50)
    Date_on_which_its_instrument_of_ratification = models.DateTimeField(
        auto_now_add=False)
    Location = models.TextField(max_length=50)

    def __str__(self):
        return self.Industry

