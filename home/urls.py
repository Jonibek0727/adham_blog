from django.urls import path
from .views import blog_single,blog_grid,homePageView, Add_comment_view

urlpatterns = [
    path('',homePageView, name='home'),
    path('blog-grid/', blog_grid.as_view(), name = 'blog-grid'),
    path('blog-single/<int:pk>', blog_single.as_view(), name = 'blog-single'),
    path('blog-single/<int:pk>/comment/', Add_comment_view.as_view(),name = 'comment'),




]