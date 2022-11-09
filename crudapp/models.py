from django.db import models

class Employee(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    des = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    city = models.CharField(max_length=30, default=None, blank=True, null=True )
    state = models.CharField(max_length=30, default=None, blank=True, null=True )

    def __str__(self):
        return str(self.ID)+" "+self.name+" "+self.des
