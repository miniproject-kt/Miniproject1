from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello, World')



from .models import Object

def getMap(request):
    
    if request.method == 'POST' and request.POST.get('stuff') != '':
        param = request.POST.get('stuff')

        stuffQuerySet = Object.objects.filter(object_name__contains=param)

        stuffs = []
        members = []
        posts = []
        for stuff in stuffQuerySet:     

            stuffs.append(stuff)

            post = stuff.posting_index
            posts.append(post)

            member = post.lender_index
            members.append(member)


        data = {
            'members': members,
            'stuffs': stuffs,
            'posts': posts
        }

        return render(request, 'borrow/map.html', data)
    return render(request, 'borrow/map.html')



def getPosting(request):
    return render(request, 'borrow/posting.html')
