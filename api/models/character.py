from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=25)

    class Classes(models.TextChoices):
        KNIGHT = 'KN', ('Knight')
        WIZARD = 'WZ', ('Wizard')
        RANGER = 'RG', ('Ranger')

    character_class = models.CharField(
        max_length=2,
        choices=Classes.choices,
        default=Classes.KNIGHT,
    )

    level = models.CharField(
        max_length=100,
        default=1,
    )

    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
      # This must return a string
        return f"The character named '{self.name}' is a level {self.level} {self.classes}."

    def as_dict(self):
        """Returns dictionary version of Character models"""
        return {
            'id': self.id,
            'name': self.name,
            'classes': self.classes,
            'level': self.level
        }
