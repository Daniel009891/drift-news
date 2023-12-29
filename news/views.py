from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Article, Comment
from .forms import CommentForm, ContactForm
from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView


def contact_form(request):

    # For custom model

    """
    Function to request the associated data from the person submitting the
    form. Checks are carried out to ensure the form is valid and all fields
    required are filled out. If this is the case the form will save to the
    database and sends this to the admin for review. Displays a message to the
    user on success. If form is not valid the built in validator will prompt
    the user to fill out the required fields.

    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your enquiry has been submitted to'
                             'admin successfully')
            return HttpResponseRedirect('/contact')
        else:
            messages.error(request, 'Error sending enquiry')

    form = ContactForm()
    context = {'form': form}

    return render(request, 'contact.html', context)


def edit_comment(request, comment_id):

    # custom function for adapted comment model from blog walkthrough

    """
    Function to edit a comment that has been left by the user. It takes the
    arguments request and comment_id so it knows the comment that is to be
    edited. If the form is valid the users updated comment will save and update
    automatically. The user is then redirected back to the corresponding
    article. A success message is displayed to the user.
    """

    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article = Article.objects.get(id=comment.article.id)
            instance.commenter = request.user
            instance.save()
            messages.success(request, 'Your comment has been'
                             'updated successfully')
            return redirect('article_detail', slug=comment.article.slug)

    else:
        form = CommentForm(instance=comment)
        messages.error(request, 'Error updating comment')

    template = 'comment_edit.html'

    context = {
        'form': form,
        'comment': comment,
    }

    return render(request, template, context)


class CommentDeleteView(DeleteView):

    # custom class for adapted comment model from blog walkthrough

    """
    Gets the model and template associated with comments. Incorporates djangos
    deleteview.

    """
    model = Comment
    template_name = 'comment_delete.html'

    def delete(self, request, *args, **kwargs):
        """
        Function to delete the users comment on the article it was origionally
        left on. it incorporates the comment delete view and deletes the
        comment. Displays a message to the user once successful.
        """
        return super(CommentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(request, 'Your comment has been deleted successfully')

    def get_success_url(self):
        """
        Function to get the success url after the comment has been deleted.
        """
        return reverse('article_detail',
                       kwargs={'slug': self.object.article.slug})


class ArticleList(generic.ListView):

    # From django blog walkthrough project# 

    """
    Details how the articles will be displayed, filtered by published so only
    published articles will be visible. Orders them by the created on date,
    newest articles first. Paginates the articles by 8 on each page.

    """
    model = Article
    queryset = Article.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8


class ArticleDetail(View):

    # From django blog walkthrough project adapted for this project

    """
    The detail view of the article elements and what is displayed to the user.

    """

    def get(self, request, slug, *args, **kwargs):

        """
        Get request function for the data of the articles that have been
        published. Gets the article objects by published status, filters
        comments by approved and orders them oldest first.
        
        """
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(
            approved=True).order_by('created_on')

        return render(
            request,
            "article_detail.html",
            {
                "article": article,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm(),

            },
        )

    def post(self, request, slug, *args, **kwargs):

        """
        post request function for comments. Displays a comment form for the
        user to fill in, if comment form is valid then the comment will be sent
        to the admin for approval. A success message is then displayed to the
        user. If form is not valid, user will be directed back to the comment
        form.
        """
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(
            approved=True).order_by('created_on')

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.commenter_id = request.user.id
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
            messages.success(request, 'Your comment has been sent to the'
                             'admins for approval')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "article_detail.html",
            {
                "article": article,
                "comments": comments,
                "commented": True,
                "comment_form": CommentForm(),

            },
        )
