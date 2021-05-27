from rest_framework import viewsets
from .serializers import EmployeeSerializer, ProfessionalSkillSerializer, EducationSerializer, CourseSerializer, ExperienceSerializer, OrganizationSerializer, SocialLinkSerializer, ApplicationSerializer, TestSerializer, QuestionSerializer, QuestionGradeSerializer, AppointmentSerializer
from .models import Employee, ProfessionalSkill, Education, Course, Experience, Organization, SocialLink, Application, Test, Question, QuestionGrade, Appointment
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('email')
    serializer_class = EmployeeSerializer
    filter_backends=(DjangoFilterBackend,)
    filter_fields=('first_name', 'middle_name', 'last_name',
			'email','password','summary','address','gender',
			'marital_status','phone','city',
			'birthday','employment','availability')

class ProfessionalSkillViewSet(viewsets.ModelViewSet):
    queryset = ProfessionalSkill.objects.all().order_by('employee')
    serializer_class = ProfessionalSkillSerializer
    filter_backends=(DjangoFilterBackend,)
    filter_fields=('level','name','category','employee','application')

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all().order_by('employee')
    serializer_class = EducationSerializer
    filter_backends=(DjangoFilterBackend,)
    filter_fields=('level','graduation_status','major',
			'university','start','end','employee','application')

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('employee')
    serializer_class = CourseSerializer
    filter_backends=(DjangoFilterBackend,)
    filter_fields=('hours','name','issuing_date','description','institute','employee')

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all().order_by('employee')
    serializer_class = ExperienceSerializer
    filter_backends=(DjangoFilterBackend,)
    filter_fields=('industry_name','summary','start_date','salary','salary_rate',
			'curruncy','job_title','company','months_of_experience','employee')

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all().order_by('email')
    serializer_class = OrganizationSerializer
    filter_backends=(DjangoFilterBackend,)
    filter_fields=('name','email','password',
				'summary','address','phone_code',
				'phone','founding_date','website','employment')

class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all().order_by('organization')
    serializer_class = SocialLinkSerializer
    filter_backends=(DjangoFilterBackend,)
    filter_fields=('facebook','linkedin','twitter','instagram','organization')

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all().order_by('organization')
    serializer_class = ApplicationSerializer
    filter_backends=(DjangoFilterBackend,)
    filter_fields=('id','name','organization',
				'role','job_title','keyword','phone','start',
				'end','vacant_position','availability',
				'months_of_experience','description','employment')

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all().order_by('organization')
    serializer_class = TestSerializer
    filter_backends=(DjangoFilterBackend,)
    filter_fields=('category','organization','end','participants','application')

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('test')
    serializer_class = QuestionSerializer
    filter_backends=(DjangoFilterBackend,)
    filter_fields=('category','question','time','grade','test')

class QuestionGradeViewSet(viewsets.ModelViewSet):
    queryset = QuestionGrade.objects.all().order_by('participant')
    serializer_class = QuestionGradeSerializer
    filter_backends=(DjangoFilterBackend,)
    filter_fields=('grade','question','participant','test')

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('organization')
    serializer_class = AppointmentSerializer
    filter_backends=(DjangoFilterBackend,)
    filter_fields=('date','availability','organization','employee','application')