from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.text import slugify

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=20, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Use slugify function on name
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

class Video(models.Model):
    id = models.CharField(max_length=100, primary_key=True, unique=True, default=uuid.uuid4,  editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='videos/thumbnail/', default='none')
    tag = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} by {self.title}"
