from django.db import models

# Create your models here.


class Link(models.Model):
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    # `<a>{}</a>` in the author section
    author_name = models.CharField(max_length=50)
    # `<a href="{}">` in the author section
    author_link = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
