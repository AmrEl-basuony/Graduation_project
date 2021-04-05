from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=256,)
    middle_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField()
    summary = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    gender = models.BooleanField()
    marital_status = models.BooleanField()
    phone = models.IntegerField()
    country = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    cv = models.FileField()
    nationality = models.CharField(max_length=256)
    FULL_TIME = 'FU'
    PART_TIME = 'PA'
    FREELANCE = 'FR'
    VOLUNTEERING = 'VO'
    TRAINING = 'TR'
    FLEXIBLE_WORK = 'FL'
    EMPLOYMENT = [
        (FULL_TIME, 'Full time'),
        (PART_TIME, 'Part time'),
        (FREELANCE, 'Freelance'),
        (VOLUNTEERING, 'Volunteering'),
        (TRAINING, 'Training'),
        (FLEXIBLE_WORK, 'Flexible work'),
    ]
    employment = models.CharField(
        max_length=2,
        choices=EMPLOYMENT,
        default=FULL_TIME,
    )
    def __str__(self):
        return self.first_name + self.middle_name + self.last_name