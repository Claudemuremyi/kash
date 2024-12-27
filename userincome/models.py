# from django.db import models
# from django.contrib.auth.models import User

# class Source(models.Model):
#     name = models.CharField(max_length=255)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.name

# class UserIncome(models.Model):
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField()
#     description = models.TextField()
#     source = models.ForeignKey(Source, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     class Meta:
#         ordering = ['-date']
        
#     def __str__(self):
#         return f"{self.source} - {self.amount}"

from django.db import models
from django.contrib.auth.models import User

class Source(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class UserIncome(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-date']
        
    def __str__(self):
        return f"{self.source} - {self.amount}"

def get_default_sources():
    return [
        "Salary", "Business", "Side-hustle", "Investments",
        "Rental Income", "Dividends", "Interest", "Gifts",
        "Freelancing", "Other"
    ]

