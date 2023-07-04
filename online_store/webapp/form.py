from django import forms

from webapp.models import Category


class CategoryForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")
    description = forms.CharField(max_length=100, required=True, label="Описание")


class GoodForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")
    description = forms.CharField(max_length=100, required=True, label="Описание")
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="(Nothing)")
    remainder = forms.IntegerField(required=True, label="Остаток товара")
    price = forms.DecimalField(required=True, label="Цена")
    image_url = forms.URLField(max_length=300, required=True, label="URL Картинки")