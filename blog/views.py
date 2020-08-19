from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.


class BlogListView(ListView):
    model = Post
    paginate_by = 4
    template_name = 'blog/blog.html'


def blog_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post).order_by('-id')
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, 
                user=request.user, 
                content=content,
                reply=comment_qs
            )
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = CommentForm()

    context = {
        'post': post,
        'form': form,
        'comments': comments
    }
    return render(request, 'blog/blog-details.html', context)
