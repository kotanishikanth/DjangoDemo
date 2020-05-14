from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.
@login_required
def home(request):
    context = { 'title': 'Posts'}

    posts = request.user.post_set.all()
    context['posts'] = posts
    return render(request, 'posts/home.html', context)
