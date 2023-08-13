from django.shortcuts import render

posts = [
    {
        'author': 'admin',
        'title': 'It''s first post',
        'content': 'First Content',
        'date_posted': '08.13.2023'
    },
    {
        'author': 'user',
        'title': 'It''s second post',
        'content': 'Second Content',
        'date_posted': '08.13.2023'
    }
]

def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',  {'title': 'Page about us'})
