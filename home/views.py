from django.shortcuts import redirect, render, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import HomePage, NEWS, Comment
from home.form import CommentForm
from django.urls import reverse_lazy


# Create your views here.
def homePageView(request):
    news = NEWS.objects.all()
    return render(request, 'index.html', {'Home_Page': HomePage.objects.all(), 'news': news})


# class Index_page(ListView):
#     model = HomePage
#     template_name = 'index.html'

class blog_grid(ListView):
    model = HomePage
    # model = Products
    template_name = 'blog-grid.html'


class blog_single(DetailView):
    model = NEWS
    template_name = 'blog-single.html'
    fields = '__all__'


class Add_comment_view(CreateView):
    model = Comment
    template_name = 'add_comments.html'
    form_class = CommentForm

    # fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')