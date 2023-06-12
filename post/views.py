from django.shortcuts import render, get_list_or_404
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from post.models import Post
from post.models import Comment
from post.forms import CommentForm, UserRegistrationForm
from post.forms import PostForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
def home_2(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post/dashboard.html', context)
def home(request):
    return render(request,'home.html')
def help_(request):
    return render(request,'help.html')
def homeDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment
            new_comment.save()
    else:
        comment_form = CommentForm()
    """try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return render(request, 'post/404.html')"""
        
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, 'news_detail.html', context)
def newPostPage(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect_to='/news/')
    else:
        form = PostForm()
    context = {
        'form' : form
    }
    return render(request=request, template_name='newpost.html', context=context)
@login_required   
def dashboard(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(
        request=request,
        template_name='post/dashboard.html',
        context=context
    )
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user= user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password2']
            )
            new_user.save()
            context = {
                'new_user':new_user
            }
            return render(
                request=request,
                template_name='post/register_done.html',
                context=context
            )
    else:
        user_form = UserRegistrationForm()
    context={
        'user_form':user_form
    }
    return render(request=request,template_name='post/register.html',context=context)