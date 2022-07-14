from django.forms import ModelForm, Textarea
from .models import Link


class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['link']

        widgets = {
            'link': Textarea(attrs={
                'placeholder': 'Вставте ссылку',
                'class': 'link_owerflow'
            })
        }
