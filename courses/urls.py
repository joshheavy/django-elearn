from django.urls import path
from .views import (
    HomePageView,
    ContactPageView,
    # SubjectListView, 
    # subjectListView,
    SubjectDetailView,
    CourseDetailView,
    InstructorPageView,
    subject_detail,
    CourseView,
    # create_course,
    # create_subject
)

app_name = 'courses'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('courses/', CourseView.as_view(), name='courses'),
    # path('subjects/', SubjectListView.as_view(), name='subjects'),
    # path('courses/<slug>/', subjectListView, name='subjects'),
    path('courses/<slug>/', CourseDetailView.as_view(), name='subjects'),
    path('courses/<course_slug>/<subject_slug>/', SubjectDetailView.as_view(), name='subject-detail'
    ),
    # path('course/create/', create_course, name='course_create'),
    path('Instructor/', InstructorPageView.as_view(), name='instructor'),
    # path('subject/create/', create_subject, name='subject_create')
]