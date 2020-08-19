from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import ReqTeacher
# Create your models here.


# relate to the publisher
class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, db_index=True)
    author = models.ForeignKey(ReqTeacher, on_delete=models.CASCADE, null=True)
    thumbnail = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:subjects', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    @property
    def get_photo_url(self):
        if self.thumbnail and hasattr(self.thumbnail, 'url'):
            return self.thumbnail.url
        else:
            return "/static/img/bg-img/e1.jpg"

    @property
    def subjects(self):
        return self.subject_set.all().order_by('-created')


# Relate to the Book
class Subject(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='courses')
    participants = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:subject-detail", kwargs={
            "course_slug": self.course.slug,
            "subject_slug": self.slug
        })
    
    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(subject=self)
        for rating in ratings:
            sum += rating.stars
            if len(ratings) > 0:
                return sum / len(ratings)
            else:
                return 0

    @property
    def get_subject_photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class Rating(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)])

    # class Meta:
    #     unique_together = [('user', 'course'), ]


class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
