from django.db import models

# Create your models here.
class Artist(models.Model):
    """Artist Model."""
    name = models.CharField(max_length=200)

    def __str__(self):
        """Get str representation.""""
        return self.name

    def __repr__(self):
        """Get str representation."""
        return self.__str__()
