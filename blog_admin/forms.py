from django import forms
from django.contrib.auth.models import User


class CreatePostForm(forms.Form):
    post_title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'نام پست جدید',
                'class': 'form-control',
            }
        ),
        label="لطفا نام پست جدید را وارد کنید."
    )

    post_simple_description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'توضیحات کوتاه پست جدید',
                'class': 'form-control',
            }
        ),
        label="لطفا توضیحات کوتاه پست جدید را وارد کنید."
    )

    post_text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'متن پست جدید',
                'class': 'form-control',
            }
        ),
        label="لطفا متن پست جدید را وارد کنید."
    )


class EditPostForm(forms.Form):
    post_title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'نام پست جدید',
                'class': 'form-control',
            }
        ),
        label="لطفا نام پست جدید را وارد کنید."
    )

    post_simple_description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'توضیحات کوتاه پست جدید',
                'class': 'form-control',
            }
        ),
        label="لطفا توضیحات کوتاه پست جدید را وارد کنید."
    )

    post_text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'متن پست جدید',
                'class': 'form-control',
            }
        ),
        label="لطفا متن پست جدید را وارد کنید."
    )


class EditSettingsForm(forms.Form):
    site_title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'نام وبلاگ ',
                'class': 'form-control',
            }
        ),
        label="لطفا نام وبلاگ را وارد کنید."
    )

    site_simple_description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'توضیحات کوتاه وبلاگ ',
                'class': 'form-control',
            }
        ),
        label="لطفا توضیحات کوتاه وبلاگ را وارد کنید."
    )

    site_copy_right_text = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'متن پست جدید',
                'class': 'form-control',
            }
        ),
        label="لطفا متن کپی رایت وبلاگ را وارد کنید."
    )


class LoginUserForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'نام کاربری ',
            'class': 'form-control',
        }
    ),
        label="لطفا نام کاربری خود را وارد کنید."
    )

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'رمز عبور',
            'class': 'form-control',
        }
    ),
        label="لطفا رمز عبور خود را وارد کنید."
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_user_found = User.objects.filter(username=user_name).exists()
        if not is_user_found:
            raise forms.ValidationError('کاربری با مشخصات وارد شده پیدا نشد')

        return user_name


class RegisterUserForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'نام کاربری ',
            'class': 'form-control',
        }
    ),
        label="لطفا نام کاربری خود را وارد کنید."
    )

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'ایمیل',
            'class': 'form-control',
        }
    ),
        label="لطفا ایمیل خود را وارد کنید."
    )

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'رمز عبور',
            'class': 'form-control',
        }
    ),
        label="لطفا رمز عبور خود را وارد کنید."
    )

    re_password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'تایید رمز عبور',
            'class': 'form-control',
        }
    ),
        label="لطفا رمز عبور خود را دوباره وارد کنید."
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_user_name_exists = User.objects.filter(username=user_name).exists()

        if is_user_name_exists:
            raise forms.ValidationError(
                'نام کاربری وارد شده موجود است.لطفا نام کاربری دیگری وارد کنید')

        return user_name

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 6:
            raise forms.ValidationError(
                'کلممه ی عبور امن نیست.لطفا رمز عبور بلند تری وارد کنید')

        return password

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('کلممه های عبور مغایرت دارند')

        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if len(email) < 10:
            raise forms.ValidationError(
                "ایمیل شما تایید نشد با ایمیل دیگری وارد شوید")

        return email


class EditUserProfileForm(forms.Form):
    user_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'نام کاربری جدید شما',
            'class': 'form-control',
        }
    ),
        label="لطفا نام کاربری جدید خود را وارد کنید."
    )

    user_first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'نام جدید شما',
            'class': 'form-control',
        }
    ),
        label="لطفا نام جدید خود را وارد کنید."
    )

    user_last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'نام خانوادگی جدید شما ',
            'class': 'form-control',
        }
    ),
        label="لطفا نام خانوادگی جدید خود را وارد کنید."
    )

    user_email = forms.EmailField(required=False, widget=forms.EmailInput(
        attrs={
            'placeholder': 'ایمیل جدید شما',
            'class': 'form-control',
        }
    ),
        label='لطفا ایمیل جدید خود را وارد کنید'
    )


class EditUserForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'نام کاربری', 'class': 'form-control'}
    ), label="لطفا نام کاربری را وارد کنید"
    )

    user_first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'نام'}
    ), label='لطفا نام را وارد کنید '
    )

    user_last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': ' نام خانوادگی '}
    ), label="لطفا نام خانوادگی را وارد کنید "
    )

    user_email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control',
               'placeholder': ' ایمیل '}
    ), label="لطفا ایمیل را وارد کنید "
    )
