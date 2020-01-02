from django.shortcuts import render

# Create your views here.
def index(request):
    posts = [
        {'id': 1, 'title': 'First Post', 'body':'This is my first post'},
        {'id': 1, 'title': 'Seconde Post', 'body':'This is my second post'},
        {'id': 1, 'title': 'Third Post', 'body':'This is my third  post'},
        ]
    return render(request, 'blog/index.html', {'posts': posts})
    