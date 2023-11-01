from django.db import models

# Create your models here.
class Record(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    publisher=models.CharField(max_length=90)
    book_name=models.CharField(max_length=90)
    class_name=models.CharField(max_length=90)
    price=models.IntegerField(max_length=50)
    quantity=models.IntegerField(max_length=50)
    sales=models.IntegerField(max_length=50)
    balance=models.IntegerField(max_length=50)

    def __str__(self):
        return (f"{self.publisher} {self.book_name}")