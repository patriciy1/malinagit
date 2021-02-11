from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    sec_name = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    main_page = models.BooleanField()

    def __str__(self):
        return self.name

    @property
    def get_products(self):
        return Product.objects.filter(categories__name=self.name)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    categories = models.ForeignKey(Category, related_name='Category', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems]) + 150
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    email = models.CharField(max_length=500, null=False)
    company = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=False)
    address = models.CharField(max_length=500, null=False)
    consent = models.CharField(max_length=200)
    question = models.CharField(max_length=200)
    note = models.TextField()
    name_2 = models.CharField(max_length=200, null=True)
    sec_name_2 = models.CharField(max_length=200, null=True)
    company_2 = models.CharField(max_length=200, null=True)
    address_2 = models.CharField(max_length=500, null=False)
    phone_2 = models.CharField(max_length=15, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


