from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class PersonalCard(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    VACCINATION_CHOICES = [('Yes', 'Yes'), ('No', 'No')]

    name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(120)]
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    vaccinated = models.CharField(max_length=3, choices=VACCINATION_CHOICES, default='No')

    def __str__(self):
        return f"{self.name} {self.middle_name or ''} {self.last_name}"

class VaccinationDetail(models.Model):
    person = models.ForeignKey(PersonalCard, on_delete=models.CASCADE, related_name="vaccinations")
    place = models.CharField(max_length=200)
    vaccination_date = models.DateField()
    vaccination_name = models.CharField(max_length=100)
    valid_until = models.DateField(null=True, blank=True)
