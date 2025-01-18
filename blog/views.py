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

    def get_queryset(self):
        """
        Process video links to extract video IDs for embedding.
        """
        posts = super().get_queryset()
        for post in posts:
            post.video_link = self.process_video_link(post.video_link)
        return posts

    def process_video_link(self, link):
        """
        Extracts video ID from YouTube or Vimeo links.
        """
        if link:
            if "vimeo.com" in link:
                return link.split("/")[-1]
            elif "youtube.com/watch?v=" in link:
                return link.split("v=")[-1]
            elif "youtu.be" in link:
                return link.split("/")[-1]
        return link    
        
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

