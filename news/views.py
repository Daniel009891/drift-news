from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Article, Comment
from .forms import CommentForm, ContactForm
from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView


def contact_form(request):

    """
    Function to request the associated data from the person submitting the form.
    Checks are carried out to ensure the form is valid and all fields required
    are filled out. If this is the case the form will save to the database and 
    send this to the admin for review.
    
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
    model = Comment
    template_name = 'comment_delete.html'

    def delete(self, request, *args, **kwargs):
        return super(CommentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(request, 'Your comment has been deleted successfully')

    def get_success_url(self):
        return reverse('article_detail',
                       kwargs={'slug': self.object.article.slug})


class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8


class ArticleDetail(View):

    def get(self, request, slug, *args, **kwargs):
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
            # messages.error(request, 'Error posting comment')

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
