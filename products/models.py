from django.db import models

# Create your models here.

category_choices = (
        
    ('Bracelets', 'Bracelets'),
    ('Necklaces', 'Necklaces'),
    ('Earings', 'Earings'),
    ('WeddingBands', 'WeddingBands'),
    ('WhiteDiamondsRings', 'WhiteDiamondsRings'),
    ('ColouredDiamondsRings', 'ColouredDiamondsRings'),
)

class Product(models.Model):
    category = models.CharField(max_length=50, choices=category_choices, default='')
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=3)
    image = models.ImageField(upload_to='images')
    
    
    def __str__(self):
        return self.name
