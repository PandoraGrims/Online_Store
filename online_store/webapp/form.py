from django import forms


class Category(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")
    description = forms.CharField(max_length=100, required=True, label="Описание")


class GoodForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")
    description = forms.CharField(max_length=100, required=True, label="Описание")
    category = forms.ForeignKey("webapp.Category", on_delete=forms.RESTRICT, verbose_name="Категория",
                                related_name="categories", null=True)
