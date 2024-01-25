from django.urls import path
from apps.comments.views import (
    CommentCreateView,
    CommentDeleteView,
    CommentUpdateView,
)


urlpatterns = [
    path('comment_create/<int:pk>',CommentCreateView.as_view(),name = 'comment_create'),
    path('comment_delete/<int:pk>',CommentDeleteView.as_view(),name = 'comment_delete'),
    path('comment_update/<int:pk>',CommentUpdateView.as_view(),name = 'comment_update'),
]
