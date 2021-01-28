from cocktails.forms import CocktailCreateForm
from cocktails.models import Alcohol, AttachedMaterial, Cocktail
from cocktails.serializers import AlcoholSerializer, AttachedMaterialSerializer, CocktailSerializer
from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework import viewsets, permissions, filters

# Create your views here.


def cocktail_index(request):
    cocktails = Cocktail.objects.order_by('name').all()

    if request.method == 'POST':
        create_form = CocktailCreateForm(request.POST, request.FILES)
        if create_form.is_valid():
            create_form.save()
            return redirect('index_cocktails')
    else:
        create_form = CocktailCreateForm()

    context = {
        'cocktails': cocktails,
        'create_form': create_form,
    }
    return render(request, 'cocktail.html', context=context)

# restful api using django restful framework


class AlcoholViewSet(viewsets.ModelViewSet):
    queryset = Alcohol.objects.all()
    serializer_class = AlcoholSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', '=alcohol_type']


class AttachedMaterialViewSet(viewsets.ModelViewSet):
    queryset = AttachedMaterial.objects.all()
    serializer_class = AttachedMaterialSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

    def get_queryset(self):
        queryset = Cocktail.objects.all()

        name = self.request.query_params.get('name', None)
        alcohol = self.request.query_params.get('alcohol', None)
        alcohol_type = self.request.query_params.get('alcohol_type', None)

        if name:
            queryset = queryset.filter(name__contains=name)
        if alcohol:
            queryset = queryset.filter(alcohols__name=alcohol)
        if alcohol_type:
            queryset = queryset.filter(alcohols__alcohol_type=alcohol_type)

        return queryset

    # permission_classes = [permissions.IsAuthenticated]
