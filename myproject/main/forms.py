from django import forms
from django.forms import modelformset_factory
from .models import TeachingMaterial, TeachingMaterialFile
from users.models import TeacherLanguage

class TeachingMaterialForm(forms.ModelForm):
    class Meta:
        model = TeachingMaterial
        fields = ['title', 'description', 'language']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'language': forms.Select(attrs={'class': 'form-select'})
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['language'].queryset = TeacherLanguage.objects.filter(
                profile__user=user)
            self.fields['language'].label_from_instance = lambda obj: obj.language.name



TeachingMaterialFileFormSet = modelformset_factory(
    TeachingMaterialFile,
    fields=('file',),
    extra=1,
    can_delete=True,
    widgets={'file': forms.ClearableFileInput(attrs={'class': 'form-control'})}
)
