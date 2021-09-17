from rest_framework import serializers

from .models import*

class ProduitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Produit
		fields = [
			"id",
			"nom",
			"slug",
			"category",
			"description",
			"prix",
			"get_image",
			"get_thumbnail",
			"get_absolute_url"
		]


class CategorieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Produit
		fields = [
		"id",
		"nom",
		"slug",
		"category",
		"description",
		"prix",
		"get_image",
		"get_thumbnail",
		"get_absolute_url"
		]