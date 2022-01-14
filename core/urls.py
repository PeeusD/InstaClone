from django.urls import path
from core import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
   #feed urls
    path('feed/', login_required(views.HomeView.as_view()), name='home_feed'),
    #following urls
    path('follow/done/', login_required(views.FollowDoneView.as_view()), name='follow_done_view'),
    path('unfollow/done/', login_required(views.UnfollowDoneView.as_view()), name='unfollow_done_view'),
    
    #post_related urls
    path('post_<int:id>', login_required(views.PostDetailView.as_view()), name='post_detail_view'),
    path('post_create/', login_required(views.PostCreateView.as_view()), name='post_create_view'),
    path('post/delete/<int:id>',login_required(views.PostDeleteView.as_view()), name='post_delete_view'),
    path('post/save/<int:id>',login_required(views.PostSaveView.as_view()), name='post_save_view'),
    path('post/unsave/<int:id>',login_required(views.PostUnsaveView.as_view()), name='post_unsave_view'),
    
    path('post/liked/', login_required(views.LikedPostView.as_view()), name='liked_posts_view'),
    path('post/explore/',login_required(views.ExplorePostView.as_view()), name='explore_posts_view'),

    path('post/like/<int:id>/', views.PostLikeView.as_view(), name='post_like_view'),
    path('post/unlike/<int:id>/', views.PostUnlikeView.as_view(), name='post_unlike_view'),
    path('post/comment/<int:id>/', views.PostCommentView.as_view(), name='post_comment_view'),
    

]
