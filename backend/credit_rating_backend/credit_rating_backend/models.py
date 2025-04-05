from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Mortgage Model using Django ORM
class Mortgage(models.Model):
    LOAN_TYPE_CHOICES = [('fixed', 'Fixed'), ('adjustable', 'Adjustable')]
    PROPERTY_TYPE_CHOICES = [('single_family', 'Single Family'), ('condo', 'Condo')]
    
    credit_score = models.IntegerField(validators=[MinValueValidator(300), MaxValueValidator(800)])
    loan_amount = models.FloatField()
    property_value = models.FloatField()
    annual_income = models.FloatField()
    debt_amount = models.FloatField()
    loan_type = models.CharField(max_length=10, choices=LOAN_TYPE_CHOICES)
    property_type = models.CharField(max_length=15, choices=PROPERTY_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    credit_rating=models.CharField(null=True,max_length=10,)

    @staticmethod
    def get_average_credit_score():
        avg_credit_score = Mortgage.objects.aggregate(models.Avg('credit_score'))['credit_score__avg']
        return avg_credit_score if avg_credit_score else 700