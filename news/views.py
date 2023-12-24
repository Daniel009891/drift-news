from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Article
from .forms import CommentForm
from django.views.generic.edit import UpdateView, DeleteView


class CommentUpdateView(UpdateView):
    model = Comment
    comment_form = CommentForm
    template_name = 'comment_update.html'
    
    def get_success_url(self):
        return reverse('article_detail', kwargs={'slug': self.object.article.slug})


class CommentDeleteView(UpdateView):
    model = Comment
    comment_form = CommentForm
    template_name = 'comment_delete.html'

    def get_success_url(self):
        return reverse('article_detail', kwargs={'slug': self.object.article.slug})


class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8


class ArticleDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(approved=True).order_by('created_on')

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
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
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
