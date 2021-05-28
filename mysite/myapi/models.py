from django.db import models
from inclusive_django_range_fields import InclusiveIntegerRangeField

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=256,)
    middle_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(unique=True,)
    password = models.CharField(max_length=256)
    image = models.ImageField(null=True)
    summary = models.CharField(max_length=256, null=True)
    address = models.CharField(max_length=256, null=True)
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
    phone = models.CharField(max_length=256,null=True)
    city = models.CharField(max_length=256, null=True)
    cv = models.FileField(null=True)
    birthday = models.DateField(null=True)
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
    employment = models.CharField(max_length=2, choices=EMPLOYMENT,default=FULL_TIME)

class Course(models.Model):
    hours = models.IntegerField(null=True) 
    name = models.CharField(max_length=256,null=True)
    issuing_date = models.DateField(null=True)
    description = models.CharField(max_length=256,null=True)
    institute = models.CharField(max_length=256,null=True)
    employee = models.ForeignKey(Employee, to_field='email', related_name='courses',on_delete=models.CASCADE,null=True)

class Experience(models.Model):
    industry_name = models.CharField(max_length=256,null=True)
    summary = models.CharField(max_length=256,null=True)
    start_date = models.DateField(null=True)	
    salary = models.IntegerField(null=True) 
    SALARY_RATE = [
            ('D', 'Daily'),
            ('W', 'Weekly'),
            ('M', 'Monthly'),
            ('Y', 'Yearly'),
        ]
    salary_rate = models.CharField(max_length=1,choices=SALARY_RATE,default='M') 
    curruncy = models.CharField(max_length=256,null=True)
    job_title = models.CharField(max_length=256,null=True)
    company = models.CharField(max_length=256,null=True)
    months_of_experience = models.IntegerField(null=True)
    employee = models.ForeignKey(Employee, to_field='email', related_name='experiences',on_delete=models.CASCADE,null=True)    

#Organization and its related models

class Organization(models.Model):
    name = models.CharField(max_length=256,)
    email = models.EmailField(unique=True,)
    password = models.CharField(max_length=256)
    image = models.ImageField(null=True)
    summary = models.CharField(max_length=256,null=True)
    address = models.CharField(max_length=256,null=True)
    phone_code = models.CharField(max_length=256,null=True)
    phone = models.CharField(max_length=256,null=True)
    founding_date = models.DateField(null=True)
    website = models.CharField(max_length=256,null=True)
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
    employment = models.CharField(max_length=2, choices=EMPLOYMENT,default=FULL_TIME)

class SocialLink(models.Model):
    facebook = models.CharField(max_length=256,null=True)
    linkedin = models.CharField(max_length=256,null=True)
    twitter = models.CharField(max_length=256,null=True)
    instagram = models.CharField(max_length=256,null=True)
    organization = models.ForeignKey(Organization,to_field='email',  related_name='socialLinks',on_delete=models.CASCADE,null=True)

#Application and its related models

class Application(models.Model):
    name = models.CharField(max_length=256,)
    organization = models.ForeignKey(Organization,to_field='email', related_name='applications', on_delete=models.CASCADE,null=True)
    image = models.ImageField(null=True)
    age_preference = InclusiveIntegerRangeField(null=True)
    role = models.CharField(max_length=256,null=True)
    job_title = models.CharField(max_length=256,null=True)
    keyword = models.CharField(max_length=256,null=True)
    phone = models.CharField(max_length=256,null=True)
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    salary_range = InclusiveIntegerRangeField(null=True,)
    vacant_position = models.CharField(max_length=256,null=True)
    AVAILABILITY = [
        (True,  'Available'),
        (False, 'Not available'),
    ]
    availability = models.BooleanField(choices=AVAILABILITY,default=True)
    months_of_experience = models.DecimalField(max_digits=10, decimal_places=5,null=True)
    description = models.CharField(max_length=256,null=True)
    job_requirements = models.CharField(max_length=256,null=True)
    GENDER_PREFERENCE = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('ANY', 'Any'),
    ]
    gender_preference = models.CharField(max_length=6, choices=GENDER_PREFERENCE,default=True)
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
    employment = models.CharField(max_length=2, choices=EMPLOYMENT,default=FULL_TIME)

class Test(models.Model):
    category = models.CharField(max_length=256,null=True)
    application = models.ForeignKey(Application, related_name='tests', on_delete=models.CASCADE,null=True)
    organization = models.ForeignKey(Organization, related_name='tests',to_field='email', on_delete=models.CASCADE,null=True)
    end = models.DateTimeField(null=True)
    participants = models.ManyToManyField(Employee,blank=True)

class Question(models.Model):
    category = models.CharField(max_length=256,null=True)
    question = models.CharField(max_length=256,null=True)
    answer = models.CharField(max_length=256,null=True)
    time  = models.DurationField(null=True)
    grade  = models.DecimalField(max_digits=10, decimal_places=5,null=True)
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE,null=True)

class QuestionGrade(models.Model):
    grade  = models.DecimalField(max_digits=10, decimal_places=5,null=True)
    question = models.ForeignKey(Question, related_name='questiongrades', on_delete=models.CASCADE,null=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE,null=True)
    participant = models.ForeignKey(Employee, related_name='questiongrades', on_delete=models.CASCADE,null=True)

class Appointment(models.Model):
    date  = models.DateField(null=True)
    AVAILABILITY = [
        (True,  'Available'),
        (False, 'Not available'),
    ]
    availability = models.BooleanField(choices=AVAILABILITY,default=True)
    application = models.ForeignKey(Application, related_name='appointments', on_delete=models.CASCADE,null=True)
    organization = models.ForeignKey(Organization, related_name='appointments', on_delete=models.CASCADE,null=True)
    employee = models.ForeignKey(Employee, related_name='appointments', on_delete=models.CASCADE,null=True)

#For multi models
class ProfessionalSkill(models.Model):
    LEVEL = [
            ('LO', 'Low'),
            ('ML', 'Mid-low'),
            ('MI', 'Middle'),
            ('MH', 'Mid-high'),
            ('HI', 'High'),
        ]
    level = models.CharField(max_length=2,choices=LEVEL,default='LO') 
    name = models.CharField(max_length=256,null=True)
    category = models.CharField(max_length=256,null=True)
    employee = models.ForeignKey(Employee, related_name='professionsalskills',to_field='email', on_delete=models.CASCADE, null=True)
    application = models.ForeignKey(Application, related_name='professionalskills', on_delete=models.CASCADE ,null=True)

class Education(models.Model):
    LEVEL = [
            ('LO', 'Bachelor\'s degree'),
            ('ML', 'Master\'s degree'),
            ('MI', 'Doctoral degree'),
        ]
    level = models.CharField(max_length=2,choices=LEVEL,default='LO') 
    GRADUATION_STATUS = [
        (True,  'Graduated'),
        (False, 'Not graduated'),
    ]
    graduation_status = models.BooleanField(choices=GRADUATION_STATUS,default=True,null=True)
    major = models.CharField(max_length=256,null=True)
    university = models.CharField(max_length=256,null=True)
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    employee = models.ForeignKey(Employee, related_name='educations',to_field='email', on_delete=models.CASCADE, null=True)
    application = models.ForeignKey(Application, related_name='educations', on_delete=models.CASCADE ,null=True)
