from django.forms import ModelForm, URLInput,Textarea
from .models import Link

class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['link']

        widgets = {
            'link': Textarea(attrs={
                'placeholder': 'Вставте ссылку',
                'class' : 'link_owerflow'
                })
            }