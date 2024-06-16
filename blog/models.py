from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    """
    This class represents a blog post in a Django application.

    Attributes:
    author: The user who created the post.
    title: The title of the post.
    text: The content of the post.
    created_date: The date and time when the post was created.
    published_date: The date and time when the post was published.
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """
        This method publishes the post by setting the published_date to the current date and time.
        """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """
        This method returns a string representation of the post.

        Returns:
        str: The title of the post.
        """
        return self.title