from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from blog_posts.models import Post
from blog_settings.models import Setting
from blog_comments.models import Comment
from .forms import AddCommentForm
from django.contrib.auth.decorators import login_required


def home_page(request):
    settings = Setting.objects.first()
    posts = Post.objects.all()
    paginator = Paginator(posts, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'settings': settings,
    }
    return render(request, 'index.html', context)


def post_detail(request, **kwargs):
    this_pk = kwargs['pk']
    this_user = request.user
    this_post = get_object_or_404(Post, pk=this_pk)
    this_comments = Comment.objects.filter(post=this_post)[::-1]
    add_comment_form = AddCommentForm(request.POST or None)

    if add_comment_form.is_valid():
        this_text = add_comment_form.cleaned_data.get('text')
        Comment.objects.create(user=this_user, post=this_post, text=this_text)
        return redirect(f"/posts/{this_pk}")

    context = {
        'post': this_post,
        'comments': this_comments,
        'add_comment_form': add_comment_form,
    }
    return render(request, 'post_detail.html', context)


@login_required(login_url='/myadmin/user-login')
def delete_comment(request, **kwargs):
    this_pk = kwargs.get('pk')
    this_user = request.user
    this_comment = get_object_or_404(Comment, pk=this_pk, user=this_user)
    this_post = this_comment.post
    print(this_post)
    print(this_post.pk)
    this_comment.delete()
    return redirect(f'/posts/{this_post.pk}')
