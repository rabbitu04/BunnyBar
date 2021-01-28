from cocktails.models import Alcohol, AttachedMaterial, Cocktail
from rest_framework import serializers


class AlcoholSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alcohol
        fields = ['id', 'name', 'alcohol_type', 'url']


class AttachedMaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AttachedMaterial
        fields = ['id', 'name', 'url']


class CocktailSerializer(serializers.HyperlinkedModelSerializer):
    alcohols = AlcoholSerializer(read_only=True, many=True)
    attached_materials = AttachedMaterialSerializer(read_only=True, many=True)

    class Meta:
        model = Cocktail
        fields = ['id', 'name', 'recipe',
                  'alcohols', 'attached_materials', 'image', 'url']
