from django import forms
from .models import Product, Version

forbidden_words = ['казино', 'криптовалюта',
                   'крипта', 'биржа',
                   'дешево', 'бесплатно',
                   'обман', 'полиция', 'радар']


class StyleInputMix:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'


class VersionForm(StyleInputMix, forms.ModelForm):
    class Meta:
        model = Version
        fields = ('version_number', 'version_name', 'is_active',)


class ProductForm(StyleInputMix, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('date_created', 'date_modified', 'user', )

    def clean_name(self):
        name = self.cleaned_data.get('name').lower()

        for word in forbidden_words:
            if word in name:
                raise forms.ValidationError("Название содержит запрещенное слово.")

        return name

    def clean_description(self):
        description = self.cleaned_data.get('description').lower()

        for word in forbidden_words:
            if word in description:
                raise forms.ValidationError("Описание содержит запрещенное слово.")

        return description
