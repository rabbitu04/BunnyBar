from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'attached-materials', views.AttachedMaterialViewSet)
router.register(r'alcohols', views.AlcoholViewSet)
router.register(r'cocktails', views.CocktailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('index/cocktails', views.cocktail_index, name='index_cocktails'),
]
