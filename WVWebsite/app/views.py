from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render

from WVWebsite.app.models import Post

NUM_OF_POSTS = 5


def render_page(request):
    return render(request, "index.html")


def home(request, username=None):
    first_name = ""
    last_name = ""
    if username:
        user = User.objects.get(username=username)
        first_name = user.first_name
        last_name = user.last_name
        post_list = Post.objects.filter(user=user)
    else:
        post_list = Post.objects.all()

    post_list = post_list.order_by("-pub_date")

    paginator = Paginator(post_list, NUM_OF_POSTS)
    page = request.GET.get("page")

    posts = paginator.get_page(page)

    return render(
        request,
        "home.html",
        {"posts": posts, "first_name": first_name, "last_name": last_name},
    )


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "body"]
    template_name = "create_post.html"
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)