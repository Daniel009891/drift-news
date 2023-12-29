from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


# adapted code institute model from blog walkthrough project

class Article(models.Model):

    """
    Model for the news articles and what data they require. The articles are
    set to display with the most recently updated first, so users can see the
    newest updates first when scrolling

    title = The title of the article

    slug = Used in conjuction of the title to allow a unique primary key for
    use later

    author = The author of the article, if the author deletes the article it
    will cascade delete any information associated with it

    Updated_on = Gets the date time now of when the article was updated, this
    will be used to show users when the article was updated.

    content = The main body of the article

    featured_image = The image displayed on the article and uploaded via the
    admin panel

    excerpt = a short extract from the article, this is not required but
    optional

    created_on = Gets the date time now of when the article was created.

    status = Will be used to set the status of the article as published or not
    published


    """
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


# adapted code institute model from blog walkthrough project for crud
# functionality

class Comment(models.Model):
    """
    Model for the creation of comments and what data they require. The ordering
    is set to the oldest comment first, so this gives users the chance to
    conversate easily.

    commenter = Data of the user leaving the comment

    article = The detail of the article the comment will be left on

    email = Email of the user leaving the comment 

    body = The main body of the comment, this will display when the comments
    are approved.

    created_on = Adate time now of when the comment was left, this allows the
    comments to be filtered accordingly.

    approved = Boolean field used to set the comment as not approved when
    submitted, admin approval required.
    """
    commenter = models.ForeignKey(
        User, on_delete=models.CASCADE,
        null=False, related_name="comment_commenter")
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments")
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.commenter}"

# custom model for user to submit a contact form to the admin


class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    subject = models.CharField(max_length=60,)
    enquiry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):

        return self.name

