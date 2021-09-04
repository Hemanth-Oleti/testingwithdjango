from django.db import models

# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255)

#     def __str__(self):
#         return self.title

# class State(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class City(models.Model):
#     state = models.ForeignKey(State, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return str(self.name)

# class Population(models.Model):
#     city = models.ForeignKey(City, on_delete=models.CASCADE)
#     population = models.PositiveIntegerField(null=True)

#     def __str__(self):
#         return str(self.city) + " - "+ str(self.population)

class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=500, null=False)
    city = models.CharField(max_length=50, null=False)
    postcode = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False, unique=True)

class Product(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    price = models.IntegerField(null=False)


class Order(models.Model):
    order_date = models.DateField(null=False)
    shipped_date = models.DateField(null=True)
    delivered_date = models.DateField(null=True)
    coupon_code = models.CharField(max_length=50, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    products = models.ManyToManyField(Product, through='LineItem')

class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False)
