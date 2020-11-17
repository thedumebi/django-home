from django.urls import path
from . import views

app_name = 'ads'
urlpatterns = [
    path('',views.AdListView.as_view(), name = 'all'),
    path('<int:pk>/detail', views.AdDetailView.as_view(), name = 'ad_detail'),
    path('create', views.AdCreateView.as_view(), name = 'ad_create'),
    path('<int:pk>/update', views.AdUpdateView.as_view(), name = 'ad_update'),
    path('<int:pk>/delete', views.AdDeleteView.as_view(), name = 'ad_delete'),
    path('<int:pk>/comment', views.CommentCreate.as_view(), name = 'ad_comment'),
    path('<int:pk>/comment/edit',views.CommentEdit.as_view(), name = 'ad_comment_edit'),
    path('<int:pk>/comment/delete', views.CommentDelete.as_view(), name = 'ad_comment_delete'),
    path('<int:pk>/picture', views.picture_file, name = 'ad_picture'),
    path('<int:pk>/favorite', views.AddFavourite.as_view(), name = 'ad_favorite'),
    path('<int:pk>/unfavorite', views.DeleteFavourite.as_view(), name = 'ad_unfavorite'),
]