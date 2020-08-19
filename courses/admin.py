from django.contrib import admin
from .models import Course, Subject, Rating, Lesson


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'thumbnail')
    prepopulated_fields = {'slug': ('title', )}


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'course')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Course, CourseAdmin)
admin.site.register(Subject)
admin.site.register(Rating)
admin.site.register(Lesson)
