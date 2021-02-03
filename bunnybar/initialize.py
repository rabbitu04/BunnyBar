from cocktails.models import Alcohol, AttachedMaterial, Cocktail
from django.shortcuts import redirect


def initialize(request):
    Alcohol.objects.all().delete()
    AttachedMaterial.objects.all().delete()
    Cocktail.objects.all().delete()

    alcohols = [
        {
            'name': '白蘭姆酒',
            'alcohol_type': 'Rum',
        }, {
            'name': '琴酒',
            'alcohol_type': 'Gin',
        }, {
            'name': '龍舌蘭酒',
            'alcohol_type': 'Tequila',
        }, {
            'name': '白蘭地',
            'alcohol_type': 'Brandy',
        }, {
            'name': '威士忌',
            'alcohol_type': 'Whisky',
        }, {
            'name': '伏特加',
            'alcohol_type': 'Vodka',
        }, {
            'name': '君度橙酒',
            'alcohol_type': 'Liqueur',
        }
    ]
    for data in alcohols:
        alcohol = Alcohol(name=data['name'], alcohol_type=data['alcohol_type'])
        alcohol.save()
    attachedMaterials = ['糖漿', '檸檬汁', '蘇打水', '可樂', '薄荷葉']
    for data in attachedMaterials:
        attachedMaterial = AttachedMaterial(name=data)
        attachedMaterial.save()
    cocktails = [
        {
            'name': 'Mojito',
            'alcohols': ['白蘭姆酒'],
            'attached_materials': ['糖漿', '檸檬汁', '薄荷葉'],
            'recipe': ['白蘭姆酒 60 ml\r\n檸檬汁 30 ml\r\n糖漿 30 ml\r\n薄荷葉 10 片\r\n蘇打水 適量']
        }
    ]

    return redirect('index_cocktails')
