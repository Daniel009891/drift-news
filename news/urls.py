from . import views
from django.urls import path


urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path("comment_delete/<int:pk>/deletecomment/",
         views.CommentDeleteView.as_view(), name="comment_delete"),
    path('comment_edit/<int:comment_id>/', views.edit_comment,
         name='comment_edit'),
]
