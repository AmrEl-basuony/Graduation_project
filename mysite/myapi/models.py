from django.db import models
from django_countries.fields import CountryField
from inclusive_django_range_fields import InclusiveIntegerRangeField

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=256,)
    middle_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    image = models.ImageField()
    summary = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    languages = CountryField(multiple=True)
    AVAILABILITY = [
        (True,  'Available'),
        (False, 'Not available'),
    ]
    availability = models.BooleanField(choices=AVAILABILITY,default=True)
    GENDER = [
        (True,  'Male'),
        (False, 'Female'),
    ]
    gender = models.BooleanField(choices=GENDER,default=True)
    MARITAL_STATUS = [
        (True,  'Married'),
        (False, 'Single'),
    ]
    marital_status = models.BooleanField(choices=MARITAL_STATUS,default=True)
    phone = models.IntegerField()
    country = CountryField()
    city = models.CharField(max_length=256)
    cv = models.FileField()
    nationality = CountryField()
    birthday = models.DateField()
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
    employment = models.CharField(max_length=2, choices=EMPLOYMENT,)
    def __str__(self):
        return self.first_name

class Course(models.Model):
    hours = models.IntegerField() 
    name = models.CharField(max_length=256,)
    issuing_date = models.DateField()
    description = models.CharField(max_length=256,)
    institute = models.CharField(max_length=256,)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Experience(models.Model):
    industry_name = models.CharField(max_length=256,)
    summary = models.CharField(max_length=256,)
    start_date = models.DateField()	
    country = CountryField()
    salary = models.IntegerField() 
    SALARY_RATE = [
            ('D', 'Daily'),
            ('W', 'Weekly'),
            ('M', 'Monthly'),
            ('Y', 'Yearly'),
        ]
    salary_rate = models.CharField(max_length=1,choices=SALARY_RATE,) 
    curruncy = models.CharField(max_length=256,)
    job_title = models.CharField(max_length=256,)
    company = models.CharField(max_length=256,)
    months_of_experience = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)    

#Organization and its related models

class Organization(models.Model):
    name = models.CharField(max_length=256,)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    image = models.ImageField()
    summary = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    phone_code = models.CharField(max_length=256)
    phone = models.IntegerField()
    founding_date = models.DateField()
    website = models.CharField(max_length=256)
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
    employment = models.CharField(max_length=2, choices=EMPLOYMENT,)

class SocialLink(models.Model):
    facebook = models.CharField(max_length=256,)
    linkedin = models.CharField(max_length=256,)
    twitter = models.CharField(max_length=256,)
    instagram = models.CharField(max_length=256,)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

#Application and its related models

class Application(models.Model):
    name = models.CharField(max_length=256,)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    age_preference = InclusiveIntegerRangeField()
    role = models.CharField(max_length=256)
    job_title = models.CharField(max_length=256)
    keyword = models.CharField(max_length=256)
    phone = models.IntegerField()
    start = models.DateField()
    end = models.DateField()
    salary_range = InclusiveIntegerRangeField()
    vacant_position = models.CharField(max_length=256)
    AVAILABILITY = [
        (True,  'Available'),
        (False, 'Not available'),
    ]
    availability = models.BooleanField(choices=AVAILABILITY,default=True)
    languages = CountryField(multiple=True)
    months_of_experience = models.DecimalField(max_digits=10, decimal_places=5)
    description = models.CharField(max_length=256)
    GENDER_PREFERENCE = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('ANY', 'Any'),
    ]
    gender_preference = models.CharField(max_length=6, choices=GENDER_PREFERENCE,)
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
    employment = models.CharField(max_length=2, choices=EMPLOYMENT,)

class Test(models.Model):
    category = models.CharField(max_length=256,)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    end = models.DateTimeField()
    participants = models.ManyToManyField(Employee,)

class Question(models.Model):
    category = models.CharField(max_length=256,)
    question = models.CharField(max_length=256,)
    answer = models.JSONField()
    time  = models.TimeField()
    grade  = models.DecimalField(max_digits=10, decimal_places=5)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

#For multi models
class ProfessionalSkill(models.Model):
    LEVEL = [
            ('LO', 'Low'),
            ('ML', 'Mid-low'),
            ('MI', 'Middle'),
            ('MH', 'Mid-high'),
            ('HI', 'High'),
        ]
    level = models.CharField(max_length=2,choices=LEVEL,) 
    name = models.CharField(max_length=256,)
    category = models.CharField(max_length=256,)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE ,null=True)

class Education(models.Model):
    LEVEL = [
            ('LO', 'Bachelor\'s degree'),
            ('ML', 'Master\'s degree'),
            ('MI', 'Doctoral degree'),
        ]
    level = models.CharField(max_length=2,choices=LEVEL,) 
    GRADUATION_STATUS = [
        (True,  'Graduated'),
        (False, 'Not graduated'),
    ]
    graduation_status = models.BooleanField(choices=GRADUATION_STATUS,default=True)
    major = models.CharField(max_length=256,)
    university = models.CharField(max_length=256,)
    country = CountryField()
    start = models.DateField()
    end = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE ,null=True)
