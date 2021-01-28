from django.contrib import admin
from cocktails.models import Alcohol, AttachedMaterial, Cocktail

# Register your models here.


class AlcoholAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'alcohol_type']


class AttachedMaterialAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class CocktailAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'alcohols_name', 'attached_materials_name']

    def alcohols_name(self, obj):
        alcohols = obj.alcohols.all()
        names = ''
        for alcohol in alcohols:
            names += alcohol.name + ', '
        return names

    def attached_materials_name(self, obj):
        attached_materials = obj.attached_materials.all()
        names = ''
        for attached_material in attached_materials:
            names += attached_material.name + ', '
        return names


admin.site.register(Alcohol, AlcoholAdmin)
admin.site.register(AttachedMaterial, AttachedMaterialAdmin)
admin.site.register(Cocktail, CocktailAdmin)
