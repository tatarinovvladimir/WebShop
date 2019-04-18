from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50, blank=False)
    desc = models.TextField(max_length=200, blank=False)
    price = models.FloatField(blank=False)
    sizes = models.CharField(blank=True, null=True, max_length=200)
    aviable = models.CharField(max_length=50, default='Нет на складе', choices=(('В наличии',"В наличии"), ("Нет на складе","Нет на складе")))
    
    def __str__(self):
        return self.name


class ItemImg(models.Model):
    img = models.ImageField(upload_to='item_images')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="imgs")

class DayItem(models.Model):
    for_item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Выберите товар")

    def __str__(self):
        return "Товар дня: " + self.for_item.name

class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    delivery = models.CharField(max_length=50)
    items = models.TextField(max_length=1000)
    date = models.DateTimeField()

    def __str__(self):
        return 'Заказ от ' + self.name

