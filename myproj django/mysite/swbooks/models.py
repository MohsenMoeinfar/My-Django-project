from django.db import models

class Book(models.Model):
  
   options = (
    ('buyer','buyer'),
    ('seller' , 'seller'),
   )
   bookname = models.CharField(max_length=110)
   author = models.CharField(max_length=110 , blank=True , null= True)
   your_name = models.CharField(max_length=110, blank=True , null= True)
   your_lastname = models.CharField(max_length=110, blank=True , null= True)
   your_university = models.CharField(max_length=110, blank=True , null= True)
   your_college = models.CharField(max_length=110, blank=True , null= True)
   detail = models.CharField(max_length=110, blank=True , null= True)
   tel_id = models.CharField(max_length=110, blank=True , null= True)
   you_are = models.CharField(max_length=110, blank=True , null= True ,choices=options)
   def __str__(self):
      return self.bookname