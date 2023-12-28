from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Article, Comment
from .forms import CommentForm, ContactForm
from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView




def edit_comment(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article = Article.objects.get(id=comment.article.id)
            instance.commenter = request.user
            instance.save()
            messages.success(request,'Your comment has been updated successfully')
            return redirect('article_detail', slug=comment.article.slug)
        

    else:
        form = CommentForm(instance=comment)

    template = 'comment_edit.html'

    context = {
        'form': form,
        'comment': comment,
    }

    return render(request, template, context)


# class CommentUpdateView(UpdateView):
#     model = Comment
#     template_name = 'comment_edit'

#     def get(self, request, body, *args, **kwargs):

#         comment = get_object_or_404(Comment, pk=pk)
#         if request.method == 'POST':
#             comment.body = request.POST.get('comment')
#             if form.is_valid():
#                 form.save()
#                 return redirect('home')
#         comment_form = CommentForm(instance=comment)
#         context = {
#             'comment_form': comment_form
#         }

#         return render(
#             request,
#             './comment_edit',
#             context,
#         )

    # def get_success_url(self):
    #     return reverse('article_detail', kwargs={'slug': self.object.article.slug})


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comment_delete.html'

    def delete(self, request, *args, **kwargs):
        return super(CommentDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('article_detail', kwargs={'slug': self.object.article.slug})
        messages.success(request,'Your comment has been deleted successfully')


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
