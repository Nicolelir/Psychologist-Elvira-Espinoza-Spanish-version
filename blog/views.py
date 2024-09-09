from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts.
    """
    queryset = Post.objects.all()
    template_name = "blog/index_blog.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**
    ``post``
        An instance of :model:`blog.Post`.

    **Template:**
    :template:`blog/post_list.html`
    """
    # Assuming 'status=1' filters published posts only
    post = get_object_or_404(Post.objects.filter(status=1), slug=slug)

    return render(
        request,
        "blog/post_list.html",
        {
            "post": post,
        },
    )

    