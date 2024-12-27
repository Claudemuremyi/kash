# from django.db import models
# from django.contrib.auth.models import User

# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     class Meta:
#         verbose_name_plural = 'Categories'
        
#     def __str__(self):
#         return self.name

# class Expense(models.Model):
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField()
#     description = models.TextField()
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     class Meta:
#         ordering = ['-date']
        
#     def __str__(self):
#         return f"{self.category} - {self.amount}"

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name

class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-date']
        
    def __str__(self):
        return f"{self.category} - {self.amount}"

def get_default_categories():
    return [
        "Food", "Transportation", "Housing", "Utilities", "Insurance",
        "Medical & Healthcare", "Saving, Investing, & Debt Payments",
        "Personal Spending", "Recreation & Entertainment", "Miscellaneous"
    ]

