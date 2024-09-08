from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError
from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    exceptions_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for exceptions_word in self.exceptions_words:
            if exceptions_word in cleaned_data.lower():
                raise ValidationError(f'В названии не должно быть слова "{exceptions_word}"')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for exceptions_word in self.exceptions_words:
            if exceptions_word in cleaned_data.lower():
                raise ValidationError(f'В описании не должно быть слова "{exceptions_word}"')
        return cleaned_data


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"

    def clean(self):
        version_indicator = self.cleaned_data.get('version_indicator')
        if version_indicator:
            active_version = Version.objects.filter(version_indicator=True)
            if self.instance.pk:
                active_version = active_version.exclude(pk=self.instance.pk)
            if active_version.exists():
                raise ValidationError('Может быть одна активная версия')
        return super().clean()
