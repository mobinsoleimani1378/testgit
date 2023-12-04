from django.db import models

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subs', blank=True, null=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

class Size(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ManyToManyField(Category, blank=True, related_name='catt')
    title = models.TextField()
    text = models.TextField(blank=True,null=True)
    price = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True)
    img = models.ImageField(upload_to="images", null=True)
    size = models.ManyToManyField(Size, blank=True, related_name="products")
    color = models.ManyToManyField(Color, related_name="products")
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    review = models.IntegerField(default=0)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

class Information_1(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE, related_name="informations")
    text = models.TextField()

    def __str__(self):
        return self.text

class AttributeMain(models.Model):
    title = models.CharField(max_length=100)
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='attributs')

    def __str__(self):
        return self.title

class AttributDetail(models.Model):
    attribute_main = models.ForeignKey(AttributeMain,on_delete=models.CASCADE, related_name='attributsdetaill')
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title