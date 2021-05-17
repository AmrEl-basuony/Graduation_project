from rest_framework import serializers
from .models import Employee, ProfessionalSkill, Education, Course, Experience, Organization, SocialLink, Application, Test, Question

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Employee
		fields = ('id', 'first_name', 'middle_name', 'last_name',
			'email','password','summary','address','gender',
			'marital_status','phone','country','city',
			'cv','nationality','birthday','employment',
			'image','availability')

class ProfessionalSkillSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ProfessionalSkill
		fields = ('level','name','category','employee','application')

class EducationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Education
		fields = ('level','graduation_status','major',
			'university','country','start','end','employee','application')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Course
		fields = ('hours','name','issuing_date','description','institute',
			'employee')

class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Experience
		fields = ('industry_name','summary','start_date','country','salary','salary_rate',
			'curruncy','job_title','company','months_of_experience','employee')

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Organization
		fields =('id','name','email','password',
				'image','summary','address','phone_code',
				'phone','founding_date','website','employment')

class SocialLinkSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SocialLink
		fields =('facebook','linkedin','twitter','instagram','organization')

class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Application
		fields =('id','name','organization',
				'age_preference','role','job_title','keyword','phone','start',
				'end','salary_range','vacant_position','availability','languages',
				'months_of_experience','description','gender_preference','employment')

class TestSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Test
		fields =('category','organization','end','participants')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Question
		fields =('category','question','answer','time','grade','test')
