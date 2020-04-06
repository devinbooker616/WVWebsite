from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render

from WVWebsite.app.models import Post


def render_page(request):
    return render(request, "index.html")


class HomeView(ListView):
    model = Post
    paginate_by = 5
    template_name = "home.html"
    context_object_name = "posts"


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "body"]
    template_name = "create_post.html"
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "body"]
    template_name = "create_post.html"
    login_url = reverse_lazy("login")

    def test_func(self):
        return Post.objects.get(id=self.kwargs["pk"]).user == self.request.user


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("Home")
    login_url = reverse_lazy("login")
    template_name = "post_confirm_delete.html"

    def test_func(self):
        return Post.objects.get(id=self.kwargs["pk"]).user == self.request.user
