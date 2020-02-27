from django import forms
from app.models import Job
from db_file_storage.form_widgets import DBClearableFileInput


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = []
        widgets = {
            'picture': DBClearableFileInput
        }
