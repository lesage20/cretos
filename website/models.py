from django.db import models

# Create your models here.
class Category_product(models.Model):
    
    
    nom = models.CharField(max_length=225, null=True)
    image = models.ImageField(upload_to='image/categorie', null=True)
    
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Category product'
        verbose_name_plural = 'Category product'

    def __str__(self):
        return self.nom


class SocialAccount(models.Model):
    ICONS = [
        ("facebook", "fa-facebook-f"),
        ("instagram", "fa-instagram"),
        ("twitter", "fa fa-twitter"),
        ("youtube", "fa fa-youtube-play")
    ]
    
    nom = models.CharField(max_length=255, null=True)
    lien = models.URLField(null=True)
    icon = models.CharField(choices=ICONS, max_length=20, null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Social account'
        verbose_name_plural = 'Socials account'

    def __str__(self):
        return self.nom


class SiteInfo(models.Model):
    email = models.EmailField(max_length=255, null=True)
    logo = models.ImageField(null=True)
    

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Site Info'
        verbose_name_plural = 'Site Infos'

    def __str__(self):
        return self.email
    
class Presentation(models.Model):
    titre = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="images", null=True)
    
    prix = models.FloatField(null=True)
    categorie_product = models.ForeignKey(Category_product, on_delete=models.CASCADE, null=True)
    

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'presentation'
        verbose_name_plural = 'presentations'
        
    def __str__(self):
        return self.titre
        
        


class Sliders(models.Model):
    titre = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="images/sliders", null=True)
    
    price = models.FloatField(null=True)
    categorie_product = models.ForeignKey(Category_product, on_delete=models.CASCADE, null=True)
    

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'

    def __str__(self):
        return self.titre


class NewsLetter(models.Model):
    email = models.EmailField(max_length=254, null=True)
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'
    
    def __str__(self):
        return self.email
 


class Contact(models.Model):
    nom = models.CharField(max_length=255, null=True)
    tel = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    message = models.TextField(blank=True, null=True)


    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.nom

class Team(models.Model):
    image = models.ImageField(upload_to="images/Team", null=True )
    titre = models.CharField(max_length=255, null=True)
    statu = models.CharField(max_length=255, null=True)


    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Team'
        verbose_name_plural = 'teams'

    def __str__(self):
        return self.titre
        

        


class Trouver_le_velo(models.Model):
    
    titre = models.CharField(max_length=255, null=True)
    type_velo = models.CharField(max_length=255, null=True)
    taille_de_roue = models.PositiveIntegerField(null=True)
    marque = models.CharField(max_length=225, null=True)
    
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'trouver le velo'
        verbose_name_plural = 'trouver le velo'

    def __str__(self):
        return self.type_velo

        





class Our_products(models.Model):
    
    
    titre = models.CharField(max_length=225, null=True)
    image = models.ImageField(upload_to='image/categorie')
    prix1 = models.FloatField(null=True)
    prix2 = models.FloatField(null=True)
    taille_du_cadre = models.PositiveIntegerField(null=True)
    nombre_de_vitesse =models.IntegerField(null=True)
    category_product = models.ForeignKey(Category_product, on_delete=models.CASCADE, null=True)
    classe = models.CharField(max_length=225)
    pays = models.CharField(max_length=225)
     

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Our_products'
        verbose_name_plural = 'Our_products'

    def __str__(self):
        return self.titre



class Feeback(models.Model):
    
    
    nom = models.CharField(max_length=225, null=True)
    image = models.ImageField(upload_to='image/categorie')
    description = models.TextField()
     

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Feeback'
        verbose_name_plural = 'Feeback'

    def __str__(self):
        return self.nom


class News(models.Model):

    nom = models.CharField(max_length=225, null=True)
    image = models.ImageField(upload_to='image/categorie')
    description = models.TextField()
    auteur = models.CharField(max_length=225, null=True)
     

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def __str__(self):
        return self.nom


class Pub(models.Model):

    titre = models.CharField(max_length=225, null=True)
    image = models.ImageField(upload_to='image/categorie')
    description = models.TextField()
    prix = models.FloatField(null=True)
     

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Pub'
        verbose_name_plural = 'Pub'

    def __str__(self):
        return self.titre


    
