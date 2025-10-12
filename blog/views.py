from django.shortcuts import render
from .models import Post
def post_list(request):
    posts = Post.objects.order_by('-published_date', '-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    return HttpResponse("Блог працює!")