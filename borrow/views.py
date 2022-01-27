from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello, World')



from .models import Member, Stuff, Post, Comment
from django.forms.models import model_to_dict

def getMap(request):
    
    if request.method == 'POST' and request.POST.get('stuff') != '':
        param = request.POST.get('stuff')

        stuffQuerySet = Stuff.objects.filter(name__contains=param)

        stuffs = []
        members = []
        posts = []
        for stuffQuery in stuffQuerySet:

            members.append(stuffQuery.member)

            stuff = model_to_dict(stuffQuery)
            stuffs.append(stuff)

            postQuerySet = Post.objects.get(stuff_name=stuff['name'])
            post = model_to_dict(postQuerySet)
            posts.append(post)

        data = {
            'members': members,
            'stuffs': stuffs,
            'posts': posts
        }

        return render(request, 'borrow/map.html', data)
    return render(request, 'borrow/map.html')





def getPosting(request):
    return render(request, 'borrow/posting.html')
