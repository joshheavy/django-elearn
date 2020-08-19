from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.core.mail import send_mail
from .forms import ProfileUpdateForm, UserUpdateForm
from .models import Profile, ReqTeacher
# Create your views here.


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'You account was successfully updated')
            return redirect('users:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, 'users/profile.html', context)

def teachRequest(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pic = request.user.profile
        create_teacher = ReqTeacher.objects.create(
            profile=pic,
            name=name,
            email=email,
            phone_num=phone
        )
        create_teacher.save()
        pic_id = pic.id 
        Profile.objects.filter(id=pic_id).update(is_teacher=True)
     
        message = 'Your request for a teacher account has been accepted! Now you can go back to Clever and upload courses and lectures, good work'
        send_mail(
            'Clever, the request was accepted.',
            message,
            'clever@no-reply.com',
            [email],
            fail_silently=False,
        )
        send_mail(
            'Clever',
            'Someone made a request on behalf of the teacher. Me info: ' + name + ' , ' + email + ' , ' + phone + ' , ' + str(pic) + '.',
            'clever@no-reply.com',
            ['joshwarurii55@gmail.com'],
            fail_silently=False,
        )
        messages.info(request, f'The request was successfully sent, you will be notified by email.')
        return redirect('courses:home')


class AccountInfo(TemplateView):
    template_name = 'users/account_info.html'

