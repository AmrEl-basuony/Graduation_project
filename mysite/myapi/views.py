from rest_framework import viewsets
from .serializers import EmployeeSerializer, ProfessionalSkillSerializer, EducationSerializer, CourseSerializer, ExperienceSerializer, OrganizationSerializer, SocialLinkSerializer, ApplicationSerializer, TestSerializer, QuestionSerializer
from .models import Employee, ProfessionalSkill, Education, Course, Experience, Organization, SocialLink, Application, Test, Question

# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer

class ProfessionalSkillViewSet(viewsets.ModelViewSet):
    queryset = ProfessionalSkill.objects.all().order_by('employee')
    serializer_class = ProfessionalSkillSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all().order_by('employee')
    serializer_class = EducationSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('employee')
    serializer_class = CourseSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all().order_by('employee')
    serializer_class = ExperienceSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all().order_by('id')
    serializer_class = OrganizationSerializer

class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all().order_by('organization')
    serializer_class = SocialLinkSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all().order_by('organization')
    serializer_class = ApplicationSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all().order_by('organization')
    serializer_class = TestSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('test')
    serializer_class = QuestionSerializer