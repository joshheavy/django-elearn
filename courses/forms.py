from django import forms
from .models import Subject, Lesson, Course


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        # fields = ('title', 'subject', 'description', 'image', 'price')
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'