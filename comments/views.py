from django.shortcuts import render

from comments.models import MaterialComments, PollComments


def index(request):
    return render(request, '', {})


def video_comments(request):
    if request.method == "POST":
        video = request.POST.get('')
        comment = request.POST.get('')

        material = Materials.objects.get(id=video)
        obj = MaterialComments.objects.create(material=material,comment=comment)

        if obj.save():
            pass

    return render(request, '', {})


def poll_comments(request):
    if request.method == "POST":
        poll = request.POST.get('')
        comment = request.POST.get('')

        poll_obj = Polls.objects.get(id=poll)
        obj = PollComments.objecs.create(poll=poll_obj,comment=comment)

        if obj.save():
            pass

    return render(request, '', {})


