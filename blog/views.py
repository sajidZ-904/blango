from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.http import HttpResponse
import logging

# Create your views here.
logger = logging.getLogger(__name__)

logger.debug("Got %d posts", len(posts))

logger.info(
    "Created comment on Post %d for user %s", post.pk, request.user
)

@cache_page(300)
@vary_on_headers("Cookie")
def index(request):
    return HttpResponse(str(request.user).encode("ascii"))
    posts = Post.objects.filter(published_at__lte=timezone.now())
    logger.debug("Got %d posts", len(posts))
    return render(request, "blog/index.html", {"posts": posts})