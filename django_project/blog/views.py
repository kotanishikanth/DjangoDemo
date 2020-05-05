from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        'title': 'HomePage',
        'posts' : [
            {'title':'One', 'author':'Subodh', 'content':'First post', 'date_posted': 'Aug 17, 2019'},
            {'title':'Two', 'author':'Mukesh', 'content':'Second post', 'date_posted': 'Aug 18, 2019'},
            {'title':'Three', 'author':'Nishikanth', 'content':'Third post', 'date_posted': 'Aug 19, 2019'},
        ]
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'About us'
    }
    return render(request, 'blog/about.html', context)