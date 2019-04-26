from django import forms
from .models import Tag
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):
    # title = forms.CharField(max_length=150)
    # slug = forms.CharField(max_length=150)

    # title.widget.attrs.update({'class':'form-control'})
    # slug.widget.attrs.update({'class':'form-control'})

    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    # кастомный метод валидатор для slug
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be \'Create\'')
        if Tag.objects.filter(slug__iexact=new_slug):
            raise ValidationError('Slug must be unique, we have {} '.format(new_slug))
        return new_slug

    # def save(self):
    #     new_tag = Tag.objects.create(
    #         title=self.cleaned_data['title'],
    #         slug=self.cleaned_data['slug']
    #     )
    #     return new_tag