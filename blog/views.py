from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts.
    """
    queryset = Post.objects.filter(estado=1).order_by("-creado_en")
    template_name = "blog/blog.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**
    ``post``
        An instance of :model:`blog.Post`.

    **Template:**
    :template:`blog/post_detalle.html`
    """
    queryset = Post.objects.filter(estado=1)
    post = get_object_or_404(queryset, slug=slug)
    return render(
        request,
        "blog/post_detalle.html",
        {"post": post},
    )