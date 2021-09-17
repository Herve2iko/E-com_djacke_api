from django.db import models
from PIL import Image
from io import BytesIO

from django.core.files import File

# Create your models here.

class Categorie(models.Model):
	nomcat = models.CharField(max_length = 30)
	slug = models.SlugField()

	class Meta:
		ordering = ('nomcat',)

	def __str__(self):
		return f'{self.nomcat}'

	def get_absolute_url(self):
		return f'/{self.slug}/'


class Produit(models.Model):
	category = models.ForeignKey(Categorie, related_name = "produit", on_delete = models.CASCADE)
	nom = models.CharField(max_length= 20)
	slug = models.SlugField()
	description = models.TextField(blank = True, null = True)
	prix = models.DecimalField(max_digits = 6, decimal_places = 2)
	image = models.ImageField(upload_to = 'upload/', blank = True, null = True)
	thumbnail = models.ImageField(upload_to = 'upload/', blank = True, null = True)
	date = models.DateField(auto_now_add = True)

	class Meta:
		ordering = ('nom',)

	def __str__(self):
		return f'{self.nom}--Category: {self.category.nomcat }'

	def get_absolute_url(self):
		return f'/{self.slug}/'

	def get_image(self):
		if self.image:
			return 'http://127.0.0.1:8000'+self.image.url
		return ''

	def get_thumbnail(self):
		if self.thumbnail:
			return 'http://127.0.0.1:8000'+self.thumbnail.url
		else:
			if self.image:
				self.thumbnail = self.make_thumbnail(self.image)
				self.save()

				return 'http://127.0.0.1:8000'+self.thumbnail.url
			else:
				return ''
	def make_thumbnail(self, image, size = (300,200)):
		img = Image.open(image)
		img.convert('RGB')
		img.thumbnail(size)
		thumb_io = BytesIO()
		img.save(thumb_io,'JPEG',quality = 85)

		thumbnail = File(thumb_io, name = image.name)

		return thumbnail