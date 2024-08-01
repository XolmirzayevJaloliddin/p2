from django.db import models
from books.models import Book
class Order(models.Model):
    STATUS_CHOICES = (
        ('new', 'Yangi buyurtma'),
        ('ready', 'Dostavkaga tayyor'),
        ('waiting', 'Yetkazilmoqda'),
        ('delivered', 'Yetkazildi'),
        ('cancelled', 'Bekor qilindi'),
    )

    CITIES = (
        ('viloyatni tanlang', 'Viloyatni tanlang'),
        ('andijan', 'Andijon viloyati'),
        ('bukhara', 'Buxoro viloyati'),
        ('fargana', "Farg'ona viloyati"),
        ("jizzakh", "Jizzax viloyati"),
        ('namangan', 'Namangan viloyati'),
        ('navoi', 'Navoiy viloyati'),
        ('kashkadarya', "Qashqadaryo viloyati"),
        ("republic of karakalpagistan", "Qoraqolpog'iston Respublikasi"),
        ("samarkand", "Samarqand viloyati"),
        ("sirdarya", "Sirdaryo viloyati"),
        ("surkhandarya", "Surxondaryo viloyati"),
        ("tashkent", "Toshkent"),
        ("khorezm", "Xorazm viloyati"),
    )
    name = models.CharField(max_length=500)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True, related_name='orders')
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=27, choices = CITIES)
    phone_number = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Task(models.Model):
    name = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
    