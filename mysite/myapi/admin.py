from django.contrib import admin
from .models import Employee, ProfessionalSkill, Education, Course, Experience, Organization, SocialLink, Application, Test, Question, QuestionGrade, Appointment

# Register your models here.
admin.site.register(Employee)
admin.site.register(ProfessionalSkill)
admin.site.register(Education)
admin.site.register(Course)
admin.site.register(Experience)
admin.site.register(Organization)
admin.site.register(SocialLink)
admin.site.register(Application)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(QuestionGrade)
admin.site.register(Appointment)
