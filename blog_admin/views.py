from django.shortcuts import get_object_or_404, redirect, render
from blog_posts.models import Post
from .forms import (
    CreatePostForm,
    EditPostForm,
    EditUserForm,
    EditUserProfileForm,
    LoginUserForm,
    EditSettingsForm,
    RegisterUserForm,
)
from blog_settings.models import Setting
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def check_user(user):
    return user.is_superuser


def set_verbose_value(empty_value, verbose_value):
    if not empty_value == '' or empty_value:
        empty_value = verbose_value


@login_required(login_url='/myadmin/user-login')
def admin_main_page(request):
    """
        return all post user for loged in user
        and return all post of weblog for super user
    """
    this_user = request.user
    if check_user(this_user):
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(user=this_user)

    context = {
        'check_user': check_user(this_user),
        'posts': posts
    }
    return render(request, 'admin/admin_main_page.html', context)


@login_required(login_url='/myadmin/user-login')
def all_users(request):
    """
        return all users for manage of superuesr
    """
    if not check_user(request.user):
        return redirect('/myadmin')

    users = User.objects.all()

    context = {'users': users}
    return render(request, 'admin/all_users.html', context)


@login_required(login_url='/myadmin/user-login')
def delete_user(request, **kwargs):
    """
        delete an users
        just for super user
    """
    if check_user(request.user):
        this_pk = kwargs['pk']
        this_user = get_object_or_404(User, pk=this_pk)
        this_user.delete()
    else:
        return redirect('/myadmin')
    return redirect('/myadmin/all-users')


@login_required(login_url='/myadmin/user-login')
def delete_post(request, **kwargs):
    """
        delete an posts just for athor post
        and delete all post for super user
    """
    this_user = request.user
    post_pk = kwargs['pk']
    if check_user(this_user):
        post = get_object_or_404(Post, pk=post_pk)
    else:
        post = get_object_or_404(Post, pk=post_pk, user=this_user)
    post.delete()

    return redirect('/myadmin')


@login_required(login_url='/myadmin/login-user')
def edit_user(request, **kwargs):
    """
        edit an users (just for super user)
    """
    if not check_user(request.user):
        return redirect('/myadmin')

    this_pk = kwargs['pk']
    this_user = get_object_or_404(User, pk=this_pk)

    edit_user_form = EditUserForm(request.POST or None)

    if edit_user_form.is_valid():
        user_name = edit_user_form.cleaned_data.get('user_name')
        user_first_name = edit_user_form.cleaned_data.get('user_first_name')
        user_last_name = edit_user_form.cleaned_data.get('user_last_name')
        user_email = edit_user_form.cleaned_data.get('user_email')

        this_user.username = user_name
        this_user.first_name = user_first_name
        this_user.last_name = user_last_name
        this_user.email = user_email
        this_user.save()

        return redirect('/myadmin/all-users')

    context = {
        'edit_user_form': edit_user_form,
        'user': this_user
    }

    return render(request, 'admin/edit_user.html', context)


@login_required(login_url='/myadmin/user-login')
def create_post(request):
    """
        submit an posts
    """
    this_user = request.user
    create_post_form = CreatePostForm(request.POST)
    if create_post_form is not None:
        if create_post_form.is_valid():
            title = create_post_form.cleaned_data.get('post_title')
            simple_description = create_post_form.cleaned_data.get(
                'post_simple_description')
            text = create_post_form.cleaned_data.get('post_text')

            Post.objects.create(
                title=title,
                simple_description=simple_description,
                text=text,
                user=this_user,
            )
            create_post_form = CreatePostForm(None)

    context = {
        'create_post_form': create_post_form,
    }
    return render(request, 'admin/create_post.html', context)


@login_required(login_url='/myadmin/user-login')
def edit_post(request, **kwargs):
    """
        edit an posts
    """
    this_user = request.user
    this_pk = kwargs['pk']
    if check_user(this_user):
        this_post = get_object_or_404(Post, pk=this_pk)
    else:
        this_post = get_object_or_404(Post, pk=this_pk, user=this_user)
    edit_post_form = EditPostForm(request.POST or None, initial={
        'post_title': this_post.title,
        'post_simple_description': this_post.simple_description,
        'post_text': this_post.text
    })
    if edit_post_form is not None:
        if edit_post_form.is_valid():
            title = edit_post_form.cleaned_data.get('post_title')
            simple_description = edit_post_form.cleaned_data.get(
                'post_simple_description')
            text = edit_post_form.cleaned_data.get('post_text')

            this_post.title = title
            this_post.simple_description = simple_description
            this_post.text = text
            this_post.save()

    context = {
        'edit_post_form': edit_post_form
    }
    return render(request, 'admin/edit_post.html', context)


@login_required(login_url="/myadmin/user-login")
def user_profile(request):
    """
        show profile for loged in user
    """
    user = request.user
    user_name = user.username
    user_email = user.email
    user_first_name = user.first_name
    user_last_name = user.last_name
    context = {
        'user_name': user_name,
        'user_email': user_email,
        'user_first_name': user_first_name,
        'user_last_name': user_last_name
    }
    return render(request, 'admin/user_profile.html', context)


@login_required(login_url='/myadmin/user-login')
def edit_user_profile(request):
    """
        edit porfile(name, family, username, email, ...) for this user
    """
    this_user = request.user

    edit_user_profile_form = EditUserProfileForm(request.POST or None)
    if edit_user_profile_form.is_valid():
        user_name = edit_user_profile_form.cleaned_data.get('user_name')
        user_first_name = edit_user_profile_form.cleaned_data.get(
            'user_first_name')
        user_last_name = edit_user_profile_form.cleaned_data.get(
            'user_last_name')
        user_email = edit_user_profile_form.cleaned_data.get('user_email')

        if user_name == "":
            user_name = this_user.username
        if user_first_name == "":
            user_first_name = this_user.first_name
        if user_last_name == "":
            user_last_name = this_user.last_name
        if user_email == "":
            user_email = this_user.email

        this_user.username = user_name
        this_user.first_name = user_first_name
        this_user.last_name = user_last_name
        this_user.email = user_email
        this_user.save()

        return redirect('/myadmin/user-profile')

    context = {
        'user': this_user,
        'edit_form': edit_user_profile_form
    }
    return render(request, 'admin/edit_user_profile.html', context)


@login_required(login_url='/myadmin/user-login')
def edit_settings(request):
    """
        edit an site settings (just for super user)
    """
    if not check_user(request.user):
        return redirect('/myadmin')

    settings = Setting.objects.first()  # set site settings if exist

    if settings is None:  # create a new site settings object if not exists
        settings = Setting.objects.create(
            title='', simple_description='', copyright_text='')
    edit_settings_form = EditSettingsForm(request.POST or None, initial={
        'site_title': settings.title,
        'site_simple_description': settings.simple_description,
        'site_copy_right_text': settings.copyright_text
    })
    if edit_settings_form is not None:
        if edit_settings_form.is_valid():
            title = edit_settings_form.cleaned_data.get('site_title')
            simple_description = edit_settings_form.cleaned_data.get(
                'site_simple_description')
            site_copy_right_text = edit_settings_form.cleaned_data.get(
                'site_copy_right_text')

            settings.title = title
            settings.simple_description = simple_description
            settings.copyright_text = site_copy_right_text
            settings.save()

    context = {
        'edit_settings_form': edit_settings_form
    }
    return render(request, 'admin/edit_settings.html', context)


def user_login(request):
    """
        login for user and super user
    """
    if request.user.is_authenticated:
        return redirect('/myadmin')

    login_user_form = LoginUserForm(request.POST or None)

    if login_user_form.is_valid():
        user_name = login_user_form.cleaned_data.get('user_name')
        password = login_user_form.cleaned_data.get('password')

        user = authenticate(request, username=user_name, password=password)

        if user is not None:
            login(request, user)
            return redirect('/myadmin')
        else:
            login_user_form.add_error(
                'user_name', 'کاربری با نام کاربری وارد شده پیدا نشد')

    context = {
        'login_form': login_user_form
    }
    return render(request, 'admin/login_user.html', context)


def user_register(request):
    """
        sign up (register) users
    """
    if request.user.is_authenticated:
        return redirect('/myadmin')

    register_user_form = RegisterUserForm(request.POST or None)

    if register_user_form.is_valid():
        user_name = register_user_form.cleaned_data.get('user_name')
        password = register_user_form.cleaned_data.get('password')
        email = register_user_form.cleaned_data.get('email')

        User.objects.create_user(
            username=user_name, email=email, password=password)

        return redirect('/myadmin/user-login')

    context = {
        'register_form': register_user_form
    }

    return render(request, 'admin/register_user.html', context)


@login_required(login_url='/myadmin/user-login')
def user_logout(request):
    """
        logout (sign out) for users and super users
    """
    logout(request)
    return redirect('/myadmin/user-login')


# render partials
def admin_header(request):
    """
        render partial view for admin header
    """
    context = {
        'title': 'ناحیه ی کاربری'
    }
    return render(request, 'admin/shared/header.html', context)


def admin_menubar(request):
    """
        render partial view for menu bar header
    """
    this_user = request.user
    is_superuser = check_user(this_user)
    context = {
        'is_superuser': is_superuser
    }
    return render(request, 'admin/shared/MenuBar.html', context)
