from django.shortcuts import render
import logging

# Create your views here.
logger = logging.getLogger(__name__)

logger.debug("Got %d posts", len(posts))

logger.info(
    "Created comment on Post %d for user %s", post.pk, request.user
)