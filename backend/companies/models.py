from django.db import models
class Company(models.Model):
    name=models.CharField(max_length=200,unique=True)
    website=models.URLField(blank=True)
    industry=models.CharField(max_length=100,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=["name"]
    def __str__(self): return self.name
