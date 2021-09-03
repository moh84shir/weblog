from django import forms


class AddCommentForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'نظر خود را در این کادر بنویسید',
            }
        ),
        label='نظر شما در رابطه با این پست'
    )
