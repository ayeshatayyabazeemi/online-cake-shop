from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Ensure unique usernames
    password = models.CharField(max_length=128)  # Store hashed passwords
    phone = models.CharField(max_length=15)  # Adjust based on your requirements
    address = models.TextField()  # Use TextField for longer addresses

    def __str__(self):
        return self.username  

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)  # Auto incrementing order ID
    username = models.ForeignKey(UserInfo, on_delete=models.CASCADE)  # Link to the user
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)  # Date and time of the order

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # Link to the order
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()




class Products(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField() 
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)

    class Meta:
        unique_together = ('name', 'category')  # Combination of name and category as primary key
        db_table = 'products'  

