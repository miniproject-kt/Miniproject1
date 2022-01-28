from django.shortcuts import render
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
