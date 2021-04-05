from rest_framework import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'first_name', 'middle_name', 'last_name','email','summary','address','gender','marital_status','phone','country','city','cv','nationality','employment')