from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=60,null=True,blank=True)
    password = models.CharField(max_length=80,null=False,blank=False)

    class Meta:
        verbose_name_plural = 'Registrations'

    def __str__(self) -> str:
        return self.name

    
