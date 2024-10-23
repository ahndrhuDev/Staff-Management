from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    age = models.IntegerField()
    photo = models.ImageField(upload_to='media', default='jpg', null=True)
    
    class Meta:
        db_table = 'employees'
        
    def __str__(self):
        return f'{self.name}'