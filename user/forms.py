from django.forms import ModelForm
from django import forms
from .models import Registration
class RegistrationForm(ModelForm):
    """Form definition for Registration."""

    class Meta:
        """Meta definition for Registrationform."""

        model = Registration
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value = True, attrs={'class':'form-control'}),
        }

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'
