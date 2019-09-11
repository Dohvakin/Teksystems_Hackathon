from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Post

# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            un=form.cleaned_data.get('username')
            messages.success(request,f'Congrats {un}, your a/c has been cr. su')
            return redirect('login')
        else:
            return render(request, 'users/register.html' ,{'form':form})
    else:
        form=UserCreationForm()
        return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    user = request.user
    user_posts = Post.objects.filter(author=request.user).order_by('-date_posted')
    template = 'users/profile.html'
    return render(request, template, {'posts':user_posts,'user': user})
    
