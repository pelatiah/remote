from django import forms
from .models import FormUse


class FormProfessiona(forms.ModelForm):
    class Meta:
        model = FormUse
        fields = ('first_name', 'last_name', 'company', 'email', 'software',
                  'training_duration_in_weeks', 'number_of_trainee',)


class FormStudent(forms.ModelForm):
    class Meta:
        model = FormUse
        fields = ('first_name', 'last_name', 'school_name', 'email', 'software',
                  'training_duration_in_weeks', 'number_of_trainee',)


class FormDesignProf(forms.ModelForm):
    class Meta:
        model = FormUse
        fields = ('first_name', 'last_name', 'company', 'email', 'software',
                  'license_type', 'detail_and_specification',)

class FormDesignself(forms.ModelForm):
    class Meta:
        model = FormUse
        fields = ('first_name', 'last_name', 'company', 'email', 'software',
                  'prefered_output', 'detail_and_specification',)

class FormInstallation(forms.ModelForm):
    class Meta:
        model = FormUse
        fields = ('first_name', 'last_name', 'company', 'email', 'software',
                  'installation_type', 'system_requirement', 'detail_and_specification')