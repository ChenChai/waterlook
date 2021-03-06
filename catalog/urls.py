from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.aboutpage, name='aboutpage'),
    path('subjects/', views.subjects, name='subjects'),
    path('courses/', views.courses, name='courses'),
    path('courses/random/', views.courseRandom, name='courseRandom'),
    path('courses/<slug:subject>/', views.subjectDetail, name='subjectDetail'),
    path('courses/<slug:subject>/<slug:code>/', views.courseDetail, name='courseDetail'),
    path('instructors/', views.InstructorListView.as_view(), name='instructors'),
    path('instructors/random/', views.instructorRandom, name='instructorRandom'),
    path('instructors/<int:instructorId>/', views.instructorDetail, name='instructorDetail'),
]
