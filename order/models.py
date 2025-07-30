from django.db import models

# Create your models here.
positions = [
    ('GOAL-KEEPER', 'Goal keeper'),
    ('DEFENDER', 'Defender'),
    ('MIDFIELDER', 'Midfielder'),
    ('FORWARD', 'Forward'),
]

gender_choices = [
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
]
class Player(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    club = models.CharField(max_length=50)
    jersey_number = models.IntegerField()
    position = models.CharField(max_length=20, choices=positions, default=positions[0][0])
    height = models.DecimalField(max_digits=3, decimal_places=1)
    gender = models.CharField(max_length=20, choices=gender_choices, default=gender_choices[0][0])
    is_academy = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} -- {self.club} ({self.position})"
    
class Meta:
    managed = False
    db_table = 'player'