from django.db import models

# Create your models here.

class Categorie(models.Model):
    """Model definition for Catégorie."""
    # TODO: Define fields here
    nom = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="image/Catégorie")

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Catégorie."""

        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'

    def __str__(self):
        """Unicode representation of Catégorie."""
        return self.nom

class Produit(models.Model):
    """Model definition for Produit."""
    # TODO: Define fields here
    nom = models.CharField(max_length=50)
    description = models.TextField()
    prix = models.PositiveIntegerField()
    image = models.ImageField(upload_to="image/Produit")
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='categorie_Product')


    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Produit."""

        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'

    def __str__(self):
        """Unicode representation of Produit."""
        return self.nom