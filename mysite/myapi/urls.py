from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'employee', views.EmployeeViewSet)
router.register(r'professionalSkill', views.ProfessionalSkillViewSet)
router.register(r'education', views.EducationViewSet)
router.register(r'course', views.CourseViewSet)
router.register(r'experience', views.ExperienceViewSet)
router.register(r'organization', views.OrganizationViewSet)
router.register(r'socialLink', views.SocialLinkViewSet)
router.register(r'application', views.ApplicationViewSet)
router.register(r'test', views.TestViewSet)
router.register(r'question', views.QuestionViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]