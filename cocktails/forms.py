from cocktails.models import Cocktail
from cocktails.models import Alcohol, AttachedMaterial, ALCOHOL_TYPES
from django import forms
from django.core.exceptions import ValidationError


class NameModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class NameModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class CocktailCreateForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    alcohol_type = forms.ChoiceField(
        required=True, choices=[(None, 'Select')] + ALCOHOL_TYPES)
    alcohol = NameModelChoiceField(
        required=True, empty_label='Select', queryset=Alcohol.objects.all())
    attached_materials = NameModelMultipleChoiceField(
        required=False, queryset=AttachedMaterial.objects.all())
    recipe = forms.CharField(
        max_length=200, widget=forms.Textarea(attrs={'rows': 8, }))
    image = forms.ImageField(required=True)

    def clean_name(self):
        name = self.cleaned_data['name']
        if Cocktail.objects.filter(name=name).exists():
            raise forms.ValidationError(
                'Cocktail "' + name + '" already exists')
        return name

    def clean_alcohol(self):
        alcohols = self.data.getlist('alcohol')
        return alcohols

    def save(self):
        cocktail = Cocktail(
            name=self.cleaned_data['name'], recipe=self.cleaned_data['recipe'], image=self.cleaned_data['image'])
        cocktail.save()
        for alcohol_id in self.cleaned_data['alcohol']:
            cocktail.alcohols.add(Alcohol.objects.get(id=alcohol_id))
        for attached_material_id in self.cleaned_data['attached_materials']:
            cocktail.attached_materials.add(
                AttachedMaterial.objects.get(id=attached_material_id))
