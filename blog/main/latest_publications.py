from .models import Blog

def latest_publications():
    return Blog.objects.all().order_by('-id')[:10]