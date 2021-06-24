from rest_framework import serializers
from .models import Employee, ProfessionalSkill, Education, Course, Experience, Organization, SocialLink, Application, Test, Question, QuestionGrade, Appointment

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Appointment
		fields =('id','date','availability','organization','employee','application')

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
	appointments = AppointmentSerializer(required=False,many=True)
	professionalSkills = ProfessionalSkillSerializer(required=False,many=True)
	educations = EducationSerializer(required=False,many=True)
	courses = CourseSerializer(required=False,many=True)
	experiences = ExperienceSerializer(required=False,many=True)
	class Meta:
		model = Employee
		fields = ('id','first_name', 'middle_name', 'last_name',
			'email','password','summary','address','gender',
			'marital_status','phone','city',
			'cv','birthday','employment',
			'image','availability','professionalSkills','educations',
			'courses','experiences','appointments')

class SocialLinkSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SocialLink
		fields =('id','facebook','linkedin','twitter','instagram','organization')

class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
	appointments = AppointmentSerializer(required=False,many=True)
	professionalskills = ProfessionalSkillSerializer(required=False,many=True)
	educations = EducationSerializer(required=False,many=True)
	class Meta:
		model = Application
		fields =('id','name','organization','job_requirements',
				'age_preference_high','age_preference_low','role','job_title','keyword','phone','start',
				'end','salary_range_high','salary_range_low','vacant_position','availability',
				'months_of_experience','description','gender_preference','employment',
				'professionalskills','educations','appointments')

class QuestionGradeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = QuestionGrade
		fields =('id','grade','question','participant','test')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
	questiongrades = QuestionGradeSerializer(required=False,many=True)
	class Meta:
		model = Question
		fields =('id','category','question','answer','time','grade','test','questiongrades')

class TestSerializer(serializers.HyperlinkedModelSerializer):
	questions = QuestionSerializer(required=False,many=True)
	class Meta:
		model = Test
		fields =('id','category','application','organization','end','participants', 'questions')

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
	appointments = AppointmentSerializer(required=False,many=True)
	socialLinks = SocialLinkSerializer(required=False,many=True)
	applications = ApplicationSerializer(required=False,many=True)
	tests = TestSerializer(required=False,many=True)
	class Meta:
		model = Organization
		fields =('id','name','email','password',
				'image','summary','address','phone_code',
				'phone','founding_date','website','employment',
				'socialLinks','applications','tests','appointments')