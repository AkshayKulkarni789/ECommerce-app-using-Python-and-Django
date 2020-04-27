from django.db import models

# Create your models here.
class Books(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	genre = models.CharField(max_length=80)
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=5)
	slug = models.SlugField(unique=True)

	def __str__(self):
		return self.title

	def snippet(self):
		return self.description[0:50] + "..."

	def get_absolute_url(self):
		return reverse('book_detail', kwargs={'slug': self.slug})
