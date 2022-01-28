from django.shortcuts import render
from .models import Lender


def getMap(request):

    if request.method == 'POST' and request.POST.get('stuff') != '':
        param = request.POST.get('stuff')

        postQuerySet = Lender.objects.filter(title__contains=param)

        members = []
        posts = []
        for post in postQuerySet:

            posts.append(post)

            member = post.lender_index
            members.append(member)


        data = {
            'posts': posts,
            'members': members
        }

        return render(request, 'borrow/map.html', data)
    return render(request, 'borrow/map.html')
