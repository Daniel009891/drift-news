from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


# adapted code institute model from blog walkthrough project

class Article(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news_article")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title


# adapted code institute model from blog walkthrough project

class Comment(models.Model):
    commenter = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, related_name="comment_commenter")
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments")
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"



# custom model for user to submit a contact form to the admin


class Contact(models.Model):
    name = models.CharField(max_length=80, blank=True)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=60, blank=True)
    enquiry = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    completed = models.BooleanField(default=False)


    def __str__(self):

        return self.name

