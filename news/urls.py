from . import views
from django.urls import path


urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path("comment_delete/<int:pk>/deletecomment/", views.CommentDeleteView.as_view(), name="comment_delete"),
    path("comment_edit/<int:pk>/editcomment/",
         views.CommentUpdateView.as_view(), name="comment_edit"),
]