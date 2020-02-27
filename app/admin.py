from django.contrib import admin
from app.models import Job, Card, PortfolioCard, PortfolioPicture, Certificate
from db_file_storage.form_widgets import DBAdminClearableFileInput
# Register your models here.
from django import forms


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = []
        widgets = {
            'picture': DBAdminClearableFileInput
        }


class PortfolioCardForm(forms.ModelForm):
    class Meta:
        model = PortfolioCard
        exclude = []
        widgets = {
            'picture': DBAdminClearableFileInput
        }


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        exclude = []
        widgets = {
            'picture': DBAdminClearableFileInput
        }


class PortfolioPictureForm(forms.ModelForm):
    class Meta:
        model = PortfolioPicture
        exclude = []
        widgets = {
            'picture': DBAdminClearableFileInput
        }


class JobAdmin(admin.ModelAdmin):
    form = JobForm


class PortfolioCardAdmin(admin.ModelAdmin):
    form = PortfolioCardForm


class PortfolioPictureAdmin(admin.ModelAdmin):
    form = PortfolioPictureForm


class CertificateAdmin(admin.ModelAdmin):
    form = CertificateForm


class CardAdmin(admin.ModelAdmin):
    model = Card


admin.site.register(Job, JobAdmin)
admin.site.register(PortfolioCard, PortfolioCardAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(PortfolioPicture, PortfolioPictureAdmin)
admin.site.register(Certificate, CertificateAdmin)
