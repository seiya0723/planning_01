from django import forms

from .models import Plan


class PlanForm(forms.ModelForm):

    class Meta:
        model   = Plan
        fields  = ["name"]


class PlanEditStaffForm(forms.ModelForm):

    class Meta:
        model   = Plan
        fields  = ["staff"]

class PlanEditManagerForm(forms.ModelForm):

    class Meta:
        model   = Plan
        fields  = ["manager"]

class PlanEditDirectorForm(forms.ModelForm):

    class Meta:
        model   = Plan
        fields  = ["director"]

class PlanEditCompanyForm(forms.ModelForm):

    class Meta:
        model   = Plan
        fields  = ["company"]




