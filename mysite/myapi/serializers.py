from rest_framework import serializers
from .models import Employee, ProfessionalSkill, Education, Course, Experience, Organization, SocialLink, Application, Test, Question, QuestionGrade, Appointment

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Appointment
		fields =('id','date','availability','organization','employee')

class ProfessionalSkillSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ProfessionalSkill
		fields = ('id','level','name','category','employee','application')

class EducationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Education
		fields = ('id','level','graduation_status','major',
			'university','start','end','employee','application')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Course
		fields = ('id','hours','name','issuing_date','description','institute',
			'employee')

class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Experience
		fields = ('id','industry_name','summary','start_date','salary','salary_rate',
			'curruncy','job_title','company','months_of_experience','employee')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
	Appointments = AppointmentSerializer(required=False,many=True)
	ProfessionalSkills = ProfessionalSkillSerializer(required=False,many=True)
	Education = EducationSerializer(required=False,many=True)
	Courses = CourseSerializer(required=False,many=True)
	Experiences = ExperienceSerializer(required=False,many=True)
	class Meta:
		model = Employee
		fields = ('first_name', 'middle_name', 'last_name',
			'email','password','summary','address','gender',
			'marital_status','phone','city',
			'cv','birthday','employment',
			'image','availability','ProfessionalSkills','Education',
			'Courses','Experiences','Appointments')

class SocialLinkSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SocialLink
		fields =('id','facebook','linkedin','twitter','instagram','organization')

class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
	ProfessionalSkills = ProfessionalSkillSerializer(required=False,many=True)
	Education = EducationSerializer(required=False,many=True)
	class Meta:
		model = Application
		fields =('id','name','organization',
				'age_preference','role','job_title','keyword','phone','start',
				'end','salary_range','vacant_position','availability',
				'months_of_experience','description','gender_preference','employment',
				'ProfessionalSkills','Education')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Question
		fields =('id','category','question','answer','time','grade','test')

class TestSerializer(serializers.HyperlinkedModelSerializer):
	Questions = QuestionSerializer(required=False,many=True)
	class Meta:
		model = Test
		fields =('id','category','organization','end','participants', 'Questions')

class QuestionGradeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = QuestionGrade
		fields =('id','grade','question','participant')

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
	Appointments = AppointmentSerializer(required=False,many=True)
	SocialLinks = SocialLinkSerializer(required=False,many=True)
	Applications = ApplicationSerializer(required=False,many=True)
	Tests = TestSerializer(required=False,many=True)
	class Meta:
		model = Organization
		fields =('name','email','password',
				'image','summary','address','phone_code',
				'phone','founding_date','website','employment',
				'SocialLinks','Applications','Tests','Appointments')