from cocktails.models import Cocktail
from cocktails.models import Alcohol, AttachedMaterial, ALCOHOL_TYPES
from django import forms
from django.core.exceptions import ValidationError

DEFAULT_OPTION = [(None, 'Select')]


class CocktailCreateForm(forms.Form):
    alcohols = Alcohol.objects.all()
    ALCOHOLS = [(alcohol.id, alcohol.name) for alcohol in alcohols]

    attached_materials = AttachedMaterial.objects.all()
    ATTACHED_MATERIALS = [(attached_material.id, attached_material.name)
                          for attached_material in attached_materials]

    name = forms.CharField(label='Name', max_length=100, required=True)
    alcohol_type = forms.ChoiceField(
        required=True, choices=DEFAULT_OPTION + ALCOHOL_TYPES)
    alcohol = forms.ChoiceField(
        required=True, choices=DEFAULT_OPTION + ALCOHOLS)
    attached_materials = forms.MultipleChoiceField(
        required=False, choices=ATTACHED_MATERIALS)
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
