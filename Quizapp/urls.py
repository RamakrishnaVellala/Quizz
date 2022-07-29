from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'quiz', views.QuizViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('home/', views.home, name="home"),
    path('register/', views.register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('addQuestion/', views.addQuestion, name='addQuestion'),
    path('quizz/', views.quizz, name='quizz'),



]
