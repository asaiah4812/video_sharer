from django.shortcuts import render, get_object_or_404
from .models import Video, Tag
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request, tag=None):
    if tag:
        videos = Video.objects.filter(tag__slug=tag)
        tag = get_object_or_404(Tag, slug=tag)
    else:
        videos = Video.objects.all()
    categories = Tag.objects.all()
    context = {
        'videos':videos,
        'tag':tag,
        'categories':categories
    }
    return render(request, 'core\home.html', context)
@login_required
def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)

    return render(request, 'core/video_detail.html', {'video':video})

