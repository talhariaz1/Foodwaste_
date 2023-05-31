from django import forms
from .models import EducationFoodWaste


class FoodWasteForm(forms.ModelForm):
    class Meta:
        model = EducationFoodWaste
        fields = "__all__"
