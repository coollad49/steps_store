from django.db import models


class Category(models.Model):
    title = models.TextField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('ordering', )

    def __str__(self):
        return self.title
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.TextField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    dateAdded = models.DateTimeField(auto_now_add=True)
    isfeatured = models.BooleanField(default=False)

    class Meta:
        ordering = ('-dateAdded',)

    def __str__(self):
        return self.title