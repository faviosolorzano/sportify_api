from django.db import models

class Team(models.Model):
    CATEGORY_CHOICES = [
        ('primera', 'Primera División'),
        ('segunda', 'Segunda División'),
        ('juvenil', 'Juvenil'),
    ]

    name     = models.CharField(max_length=100)
    city     = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Player(models.Model):
    POSITION_CHOICES = [
        ('portero',    'Portero'),
        ('defensa',    'Defensa'),
        ('mediocampo', 'Mediocampo'),
        ('delantero',  'Delantero'),
    ]

    team          = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    name          = models.CharField(max_length=100)
    position      = models.CharField(max_length=20, choices=POSITION_CHOICES)
    shirt_number  = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.team.name})"