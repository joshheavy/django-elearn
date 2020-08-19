from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
from django.views import View
from courses.models import Course, Rating, Subject, Lesson
from courses.forms import CourseForm, LessonForm, SubjectForm
from blog.models import Post
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subjects = Subject.objects.all()[:3]
        posts = Post.objects.all()[:2]
        context['subjects'] = subjects
        context['posts'] = posts
        return context
       

class ContactPageView(TemplateView):
    template_name = 'blog/contact.html'


class InstructorPageView(TemplateView):
    template_name = 'users/instructor.html'


# class SubjectListView(ListView):
#     model = Subject
#     paginate_by = 3
#     template_name = 'courses/subjects.html'

# def subjectListView(request, slug):
#     course = get_object_or_404(Course, slug=slug)
#     subjects = Subject.objects.filter(course=course)
#     courses = Course.objects.all()
#     template = 'courses/subjects.html'
#     context = {
#         'subjects': subjects,
#         'courses': courses
#     }
#     if not subjects:
#         return HttpResponse("Subjects coming soon")
#     return render(request, template, context)


# class SubjectDetailView(View):
#     def get(self, request, slug, subject_slug, *args, **kwargs):
#         # course_qs = Course.objects.filter(slug=course_slug)
        
#         # if course_qs.exists():
#         #     course = course_qs.first()

#         # subject_qs = course.subjects.filter(slug=subject_slug)
#         # if subject_qs.exists():
#         #     subject = subject_qs.first()
#         course = get_object_or_404(Course, slug=self.kwargs['slug'])
#         subjects = Subject.objects.filter(course=course)
        
#         if subjects.exists():
#             subject = course.subjects.filter(slug=subject_slug)

#         context = {
#             'object': subject
#         }      
#         return render(request, 'courses/single_subject.html', context)


class CourseView(View):
    def get(self, *args, **kwargs):
        courses = Course.objects.all()
        context = {
            'courses': courses
        }
        return render(self.request, 'courses/courses.html', context)


class CourseDetailView(ListView):
    template_name = 'courses/subjects.html'

    def get_queryset(self):
        # i want to return all the subjects for this specific course
        # return all the books based on specific publisher
        self.course = get_object_or_404(Course, slug=self.kwargs['slug'])
        return Subject.objects.filter(course=self.course)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = self.course
        return context


class SubjectDetailView(View):
    def get(self, request, course_slug, subject_slug):
        course = get_object_or_404(Course, slug=course_slug)
        subject = get_object_or_404(Subject, slug=subject_slug)
        context = {'obj': subject}
        return render(request, "courses/single_subject.html", context)


# class SubjectDetailView(DetailView):
#     template_name = 'courses/single_subject.html'
#     model = Subject

#     # def get_object(self, queryset=None):
#     #     if queryset is None:
#     #         queryset = self.get_queryset()

#     def get_object(self):
#         course_slug = self.kwargs.get('course_slug', None)
#         subject_slug = self.kwargs.get('subject_slug', None)

#         self.course = get_object_or_404(Course, slug=course_slug)
#         queryset = Subject.objects.filter(course=self.course)

#         if queryset is None:
#             queryset = self.queryset

#         try:
#             obj = queryset.get(course__slug=course_slug, slug=subject_slug)
#         except queryset.model.DoesNotExist:
#             raise Http404("No subject found matching the query")
#         return obj




    # def get_object(self):
    #     course = get_object_or_404(Course, slug=self.kwargs['slug'])
    #     subject = Subject.objects.filter(course=course)
    #     if subject:
    #         course_slug = self.kwargs.get('course_slug', None)
    #         subject_slug = self.kwargs.get('subject_slug', None)

# def create_subject(request):
#     if not request.user.profile.is_teacher == True:
#         messages.error(request, f'Your account does not have access to this page only teachers accounts!')
#         return redirect('courses:home')
#     if request.method == 'POST':
#         form = SubjectForm(request.POST or None)
#         if form.is_valid():
#             messages.success(request, 'You Subject was created')
#             return redirect('courses:course_create')
#     else:
#         form = SubjectForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'courses/create_subject.html', context)


# def create_course(request):
#     if not request.user.profile.is_teacher == True:
#         messages.error(request, f'Your account does not have access to this page only teachers accounts!')
#         return redirect('courses:home')
#     if request.method == 'POST':
#         form = CourseForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             form.save()
#             messages.success('Your class was created')
#             return redirect('courses:home')
#     else:
#         form = CourseForm()  
#     context = {
#         'form': form
#     }
#     return render(request, 'courses/create_course.html', context)

def subject_detail(request, slug):
    subject = get_object_or_404(Subject, slug=slug)
    context = {
        'subject': subject,
    }
    return render(request, 'courses/single_subject.html', context)
