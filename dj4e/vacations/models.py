from django.db import models
from django.core.validators import MinLengthValidator

class Location(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Location must be greater than 1 character")]
    )

    def __str__(self):
        return self.name

class Trip(models.Model):
    nickname = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )
    length = models.PositiveIntegerField()
    hotel = models.CharField(max_length=300)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname
